#! /usr/bin/env python

from sys import exit, argv, stderr
from socket import socket
from pickle import load
from course import Course
from book import Book

def main():

    if len(argv) != 3:
        print('Usage: python %s host port' % argv[0])
        exit(1)

    try:
        host = argv[1]
        port = int(argv[2])

        with socket() as sock:
            sock.connect((host, port))
            flo = sock.makefile(mode = 'rb')

            courses = []

            for _ in range(2):
                course_name = load(flo)
                book_title = load(flo)
                book_price = load(flo)
                book = Book(book_title, book_price)
                course = Course(course_name, book)
                courses.append(course)

        for course in courses:
            print(course)

    except Exception as ex:
        print(ex, file=stderr)
        exit(1)

if __name__ == '__main__':
    main()
