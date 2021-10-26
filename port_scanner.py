import socket
import threading
import sys

from time import sleep


def port_check(ip, port):
    try:
        s = socket.socket()
        s.connect((ip, int(port)))
        print(str(port), " open padah hua ha")

    except:
        pass


def main():
    if len(sys.argv) != 2:
        print("IP to do")
        exit(1)

    ip = sys.argv[1]
    threads = []

    for port in range(1, 65535):
        t = threading.Thread(target=port_check, args=(ip, port))
        threads.append(t.start())
        sleep(0.01)

    for t in threads:
        t.join()


main()
