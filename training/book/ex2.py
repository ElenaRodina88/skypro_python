from book import Book

book1 = Book('Harry Potter', 'Joan Rowling')
book2 = Book('The Lord Of The Ring', 'John Tolkien')
book3 = Book('Duna', 'Frank Herbert')

library = [book1, book2, book3]

for book in library:
    print(f'{book.name} - {book.author}')
