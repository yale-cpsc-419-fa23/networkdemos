#! /usr/bin/env python

from os import name
from sys import exit, argv, stderr
from socket import socket, SOL_SOCKET, SO_REUSEADDR
from time import localtime, asctime

def handle_client(sock):

    datetime = asctime(localtime())
    flo = sock.makefile(mode='w', encoding='ascii')
    flo.write(datetime + '\n')
    flo.flush()

def main():

    if len(argv) != 2:
        print('Usage: python %s port' % argv[0])
        exit(1)

    try:
        port = int(argv[1])

        server_sock = socket()
        print('Opened server socket')
        if name != 'nt':
            server_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        server_sock.bind(('', port))
        print('Bound server socket to port')
        server_sock.listen()
        print('Listening')

        while True:
            try:
                sock, client_addr = server_sock.accept()
                with sock:
                    print('Accepted connection')
                    print('Opened socket')
                    print('Server IP addr and port:',
                        sock.getsockname())
                    print('Client IP addr and port:', client_addr)
                    handle_client(sock)
            except Exception as ex:
                print(ex, file=stderr)

    except Exception as ex:
        print(ex, file=stderr)
        exit(1)

if __name__ == '__main__':
    main()