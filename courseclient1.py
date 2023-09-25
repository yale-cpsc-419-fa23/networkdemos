#! /usr/bin/env python

from sys import exit, argv, stderr
from socket import socket
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
            flo = sock.makefile(mode = 'r', encoding='utf-8')

            courses = []

            for _ in range(2):
                course_name = flo.readline()
                if course_name == '':
                    raise Exception('Ran out of input')
                course_name = course_name.rstrip()

                book_title = flo.readline()
                if book_title == '':
                    raise Exception('Ran out of input')
                book_title = book_title.rstrip()

                book_price = flo.readline()
                if book_price == '':
                    raise Exception('Ran out of input')
                book_price = book_price.rstrip()

                book = Book(book_title, float(book_price))
                course = Course(course_name, book)
                courses.append(course)

        for course in courses:
            print(course)

    except Exception as ex:
        print(ex, file=stderr)
        exit(1)

if __name__ == '__main__':
    main()
