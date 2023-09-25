#! /usr/bin/env python

from os import name
from sys import exit, argv, stderr
from socket import socket, SOL_SOCKET, SO_REUSEADDR
from book import Book
from course import Course

def handle_client(sock):
    book1 = Book('Compilers: Principles ...', 88.55)
    book2 = Book('The Practice of Programming', 35.14)
    course1 = Course('CPSC 421', book1)
    course2 = Course('CPSC 419', book2)
    courses = [course1, course2]
    
    flo = sock.makefile(mode='w', encoding='utf-8')
    for course in courses:
        flo.write(course.get_name() + '\n')
        book = course.get_book()
        flo.write(book.get_title() + '\n')
        flo.write(str(book.get_price()) + '\n')
    flo.flush()
    print('Wrote courses to client')

def main():

    if len(argv) != 2:
        print('Usage: python %s port' % argv[0])
        exit(1)
    try:
        port = int(argv[1])
        server_sock = socket()
        if name != 'nt':
            server_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        server_sock.bind(('', port))
        server_sock.listen()
        while True:
            try:
                sock, client_addr = server_sock.accept()
                with sock:
                    handle_client(sock)
            except Exception as ex:
                print(ex, file=stderr)
    except Exception as ex:
        print(ex, file=stderr)
        exit(1)

if __name__ == '__main__':
    main()
