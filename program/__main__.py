from handler import Handler
from scanner import Scanner

def main():
    args_handler = Handler()
    ip = args_handler.parsing_ip()

    tgt.send('1.1.1.1')
    scan = Scanner(tgt)
    scan.scan_ports()

if __name__ == "__main__":
    main()
