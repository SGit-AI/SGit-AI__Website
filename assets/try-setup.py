# sgit.ai /try page — in-browser runtime setup.
# Runs once after the sgit-ai wheel is installed under Pyodide:
#   1. installs the XHR network transport (Pyodide has no sockets, so urllib's
#      urlopen is rerouted through the browser's synchronous XMLHttpRequest —
#      which also means CORS applies, and the SG/Send servers allow it)
#   2. defines __sh(), the little shell behind the terminal UI: a busybox of
#      file commands over Pyodide's in-memory filesystem, plus real `sgit ...`
#      commands run in-process against the installed package.
import io, os, re, sys, shlex, shutil, contextlib


# ---------- 0. serial executor (Pyodide cannot spawn threads) ----------
# sgit parallelises blob transfers with ThreadPoolExecutor; under WebAssembly
# thread creation fails ("can't start new thread"). All call sites import the
# executor at call time, so one global swap makes every transfer path serial.
# Verified natively against the live server with thread creation disabled:
# full 225-blob clone, byte-correct.
def _install_serial_executor():
    import concurrent.futures as _cf

    class _SerialExecutor:
        def __init__(self, max_workers=None, **kw):
            pass
        def submit(self, fn, *a, **kw):
            f = _cf.Future()
            try:
                f.set_result(fn(*a, **kw))
            except BaseException as e:
                f.set_exception(e)
            return f
        def map(self, fn, *iterables, timeout=None, chunksize=1):
            return map(fn, *iterables)
        def shutdown(self, wait=True, **kw):
            pass
        def __enter__(self):
            return self
        def __exit__(self, *a):
            return False

    _cf.ThreadPoolExecutor = _SerialExecutor


if sys.platform == 'emscripten':
    _install_serial_executor()


# ---------- 1. XHR transport ----------
def _install_xhr_transport():
    import sgit_ai.network.api.Vault__API as vapi
    from urllib.error import HTTPError
    from js import XMLHttpRequest
    from pyodide.ffi import to_js

    class _Resp(io.BytesIO):
        def __init__(self, data, status):
            super().__init__(data)
            self.status = status
        def __enter__(self):
            return self
        def __exit__(self, *a):
            return False
        def getcode(self):
            return self.status

    def _xhr_urlopen(req, timeout=None, context=None, **kw):
        if isinstance(req, str):
            url, method, headers, data = req, 'GET', {}, None
        else:
            url     = req.full_url
            method  = req.get_method()
            headers = dict(req.header_items())
            data    = req.data
        xhr = XMLHttpRequest.new()
        xhr.open(method, url, False)                      # synchronous — the page freezes briefly
        xhr.overrideMimeType('text/plain; charset=x-user-defined')
        for k, v in headers.items():
            if k.lower() == 'x-api-key':
                # sgit sends the token on BOTH x-sgraph-access-token and X-API-Key
                # (native-CLI compat). The servers' CORS allow-list has the former
                # but not the latter, and a disallowed header fails the whole
                # preflight — so the browser transport drops the redundant one.
                continue
            xhr.setRequestHeader(k, str(v))
        try:
            if data:
                xhr.send(to_js(bytearray(data)))
            else:
                xhr.send()
        except Exception as e:
            raise HTTPError(url, 599, 'browser blocked the request (CORS or network): %s' % e, {}, io.BytesIO(b''))
        raw    = bytes(ord(c) & 0xFF for c in xhr.responseText)
        status = int(xhr.status)
        if status == 0:
            raise HTTPError(url, 599, 'network unreachable (blocked by the browser?)', {}, io.BytesIO(b''))
        if status >= 400:
            raise HTTPError(url, status, 'HTTP %d' % status, {}, io.BytesIO(raw))
        return _Resp(raw, status)

    vapi.urlopen = _xhr_urlopen


_install_xhr_transport()

# ---------- 2. workspace ----------
os.makedirs('/workspace', exist_ok=True)
os.chdir('/workspace')

_HELP = '''sgit.ai in-browser terminal — everything runs in this tab's memory filesystem.

  sgit <command> [...]   the real sgit CLI, in-process (try: sgit help all)
                         network commands (clone/push/pull/doctor) use the
                         browser's own HTTP — the page freezes while they run
  ls [-a] [path]         list files          cat <file>        print a file
  cd [path]              change directory    head [-n N] <f>   first lines
  pwd                    where am I          tree [path]       directory tree
  mkdir <dir>            make directory      echo txt > file   write a file
  rm [-r] <path>         remove              cp / mv <a> <b>   copy / move
  touch <file>           empty file          clear             clear the screen
  help                   this text

Notes: the filesystem is ephemeral — gone on refresh (the remote vault you push
to persists). Confirmation prompts can't be answered here; use flags like
--yes where a command offers them. Write operations need --token <token>.'''


def _fmt_size(n):
    for unit in ('B', 'K', 'M'):
        if n < 1024 or unit == 'M':
            return ('%d%s' % (n, unit)) if unit == 'B' else ('%.1f%s' % (n, unit))
        n = n / 1024.0
    return str(n)


def _ls(args):
    show_all = '-a' in args or '-la' in args or '-al' in args
    paths = [a for a in args if not a.startswith('-')] or ['.']
    out = []
    for p in paths:
        if not os.path.exists(p):
            out.append('ls: no such path: ' + p)
            continue
        if os.path.isfile(p):
            out.append(p)
            continue
        entries = sorted(os.listdir(p))
        if not show_all:
            entries = [e for e in entries if not e.startswith('.')]
        if len(paths) > 1:
            out.append(p + ':')
        for e in entries:
            full = os.path.join(p, e)
            if os.path.isdir(full):
                out.append('  %-36s  <dir>' % (e + '/'))
            else:
                try:
                    out.append('  %-36s  %s' % (e, _fmt_size(os.path.getsize(full))))
                except OSError:
                    out.append('  ' + e)
        if not entries:
            out.append('  (empty)')
    return '\n'.join(out)


def _tree(root, prefix='', budget=None):
    if budget is None:
        budget = [300]
    lines = []
    try:
        entries = sorted(os.listdir(root))
    except OSError as e:
        return [prefix + '!! ' + str(e)]
    for i, e in enumerate(entries):
        if budget[0] <= 0:
            lines.append(prefix + '… (truncated)')
            break
        budget[0] -= 1
        full = os.path.join(root, e)
        tee = '└─ ' if i == len(entries) - 1 else '├─ '
        lines.append(prefix + tee + e + ('/' if os.path.isdir(full) else ''))
        if os.path.isdir(full):
            ext = '   ' if i == len(entries) - 1 else '│  '
            lines.extend(_tree(full, prefix + ext, budget))
    return lines


def _run_sgit(args):
    from sgit_ai.cli import main as _sgit_main
    buf, old_argv = io.StringIO(), sys.argv
    sys.argv = ['sgit'] + args
    code = 0
    try:
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
            _sgit_main()
    except SystemExit as e:
        code = e.code if isinstance(e.code, int) else 0
    except Exception as e:
        buf.write('error: %r\n' % (e,))
        code = 1
    finally:
        sys.argv = old_argv
    out = buf.getvalue()
    out = '\n'.join(ln.split('\r')[-1] for ln in out.split('\n'))   # collapse \r progress
    out = re.sub(r'\x1b\[[0-9;]*m', '', out)                        # strip ANSI colours
    if code not in (0, None):
        out = out.rstrip('\n') + '\n(exit %s)' % code
    return out.rstrip('\n')


def __sh(line):
    line = (line or '').strip()
    if not line:
        return ''
    try:
        parts = shlex.split(line)
    except ValueError as e:
        return 'parse error: %s' % e
    cmd, args = parts[0], parts[1:]
    try:
        if cmd == 'help':
            return _HELP
        if cmd == 'clear':
            return '\x00__CLEAR__'
        if cmd == 'pwd':
            return os.getcwd()
        if cmd == 'cd':
            os.chdir(args[0] if args else '/workspace')
            return ''
        if cmd == 'ls':
            return _ls(args)
        if cmd == 'tree':
            root = args[0] if args else '.'
            return root + '\n' + '\n'.join(_tree(root))
        if cmd == 'mkdir':
            for a in args:
                os.makedirs(a, exist_ok=True)
            return ''
        if cmd == 'touch':
            for a in args:
                open(a, 'a').close()
            return ''
        if cmd == 'rm':
            recursive = '-r' in args or '-rf' in args
            for a in [x for x in args if not x.startswith('-')]:
                if os.path.isdir(a):
                    if recursive:
                        shutil.rmtree(a)
                    else:
                        return 'rm: %s is a directory (use rm -r)' % a
                elif os.path.exists(a):
                    os.remove(a)
                else:
                    return 'rm: no such file: ' + a
            return ''
        if cmd == 'cp':
            (shutil.copytree if os.path.isdir(args[0]) else shutil.copy2)(args[0], args[1])
            return ''
        if cmd == 'mv':
            shutil.move(args[0], args[1])
            return ''
        if cmd in ('cat', 'head'):
            n = 10
            if cmd == 'head' and '-n' in args:
                i = args.index('-n')
                n = int(args[i + 1])
                args = args[:i] + args[i + 2:]
            outs = []
            for a in args:
                data = open(a, 'rb').read()
                try:
                    text = data.decode('utf-8')
                except UnicodeDecodeError:
                    outs.append('%s: binary file (%d bytes)' % (a, len(data)))
                    continue
                outs.append('\n'.join(text.split('\n')[:n]) if cmd == 'head' else text)
            return '\n'.join(outs)
        if cmd == 'echo':
            redir = None
            for op in ('>>', '>'):
                if op in args:
                    i = args.index(op)
                    redir = (op, args[i + 1])
                    args = args[:i]
                    break
            text = ' '.join(args)
            if redir:
                with open(redir[1], 'a' if redir[0] == '>>' else 'w') as f:
                    f.write(text + '\n')
                return ''
            return text
        if cmd == 'date':
            import datetime
            return datetime.datetime.now(datetime.timezone.utc).isoformat()
        if cmd == 'whoami':
            return 'you, in your own browser — no server involved'
        if cmd in ('sgit', 'sgit-ai'):
            return _run_sgit(args)
        return "%s: not a command here (try 'help' — or the Python console below)" % cmd
    except Exception as e:
        return 'error: %r' % (e,)


'terminal ready'
