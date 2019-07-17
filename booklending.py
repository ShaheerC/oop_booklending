import random
from datetime import datetime

class Book:

    on_shelf = []
    on_loan = []

    def __init__ (self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
    
    @classmethod
    def create (cls):
        new_book = Book() #have to provide arguments (title author isbn) to the book
        cls.on_shelf.append(new_book)
        return new_book

    @classmethod
    def browse (cls):
        return random.choice(Book.on_shelf)

    