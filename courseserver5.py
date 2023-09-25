#! /usr/bin/env python

from os import name
from sys import exit, argv, stderr
from socket import socket, SOL_SOCKET, SO_REUSEADDR
from pickle import dump
from book import Book
from course import Course

def handle_client(sock: socket):
    book1 = Book('The Practice of Programming', 35.14)
    course1 = Course('CPSC 419', book1)  # Shared book
    course2 = Course('CPSC 439', book1)  # Shared book
    courses = [course1, course2]

    with sock.makefile(mode='wb') as flo:
        for course in courses:
            dump(course, flo)
        flo.flush()
    print('Wrote courses to client')

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
        print(f'Listening on port {port}')
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
