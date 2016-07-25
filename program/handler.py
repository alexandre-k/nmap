import argparse

def coroutine(func):
        def inner(*args, **kwargs):
            f = func(*args, **kwargs)
            next(f)
            return f
        return inner

class Handler(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Scan opened well-known ports')
        self.parser.add_argument('-i', '--ip', default=None, help='IPs to scan', type=str, nargs='+')
        self.parser.add_argument('-r', '--range', default=None, help='Range of IPs to scan', type=str)
        self.parser.add_argument('-hn', '--hostname', default=None, help='Hostname(s) to be scanned', type=str, nargs='+')
        self.args = self.parser.parse_args(namespace=self)

    def parsing_ip(self):
        mylist = ['1.1.1.1']
        for tgt in mylist:
            yield tgt
            print(tgt)

    def parsing_range(self):
        pass

    def parsing_hostname(self):
        pass
