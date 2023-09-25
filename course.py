class Course:
    def __init__(self, name, book):
        self._name = name
        self._book = book

    def __str__(self):
        return self._name + '\n' + str(self._book) + '\n'

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_book(self, book):
        self._book = book

    def get_book(self):
        return self._book
