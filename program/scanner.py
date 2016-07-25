def coroutine(func):
        def inner(*args, **kwargs):
            f = func(*args, **kwargs)
            next(f)
            return f
        return inner

class Scanner(object):
    def __init__(self, tgt=None):
        self.tgt = tgt

    @coroutine
    def scan_ports(self):
        print('[+] Scanning well-known ports for {}'.format(self.ip))
        well_known_ports = (port for ports in range(0,1024))
        for port in well_known_ports:
            ip = (yield)
            print(ip, port)


