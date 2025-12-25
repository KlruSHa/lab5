from collections_utils import BookCollection, IndexDict
from errors import DuplicateBookError, BookNotFoundError


class Library:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.books = BookCollection()
        self.by_author = IndexDict()
        self.by_year = IndexDict()
        self.by_genre = IndexDict()
        self.by_isbn = IndexDict()

    def __contains__(self, isbn):
        return len(self.by_isbn[isbn]) > 0

    def __repr__(self):
        return f"<Library: всего {len(self.books)} книг (индексов: {len(self.by_author)} авторов)>"

    def add_book(self, book):
        if book.isbn in self:
            raise DuplicateBookError(f"Книга с {book.isbn} уже существует")
        self.books.add_book(book)
        self.by_author.add_to_index(book.author, book)
        self.by_isbn.add_to_index(book.isbn, book)
        self.by_year.add_to_index(book.year, book)
        self.by_genre.add_to_index(book.genre, book)
        print(f"Добавлена книга: {book.title} | Автор: {book.author} | Год: {book.year} | Жанр: {book.genre} | ISBN: {book.isbn}")

    def remove_book(self, book_or_isbn):
        if isinstance(book_or_isbn, str):
            books_found = self.by_isbn[book_or_isbn]
            if not books_found:
                raise BookNotFoundError(f"Книга с ISBN {book_or_isbn} не найдена.")
            target_book = books_found[0]
        else:
            target_book = book_or_isbn
        self.books.remove_book(target_book)
        self.by_author.remove_from_index(target_book.author, target_book)
        self.by_isbn.remove_from_index(target_book.isbn, target_book)
        self.by_year.remove_from_index(target_book.year, target_book)
        self.by_genre.remove_from_index(target_book.genre, target_book)
        print(f"Удалена книга: {target_book.title} | Автор: {target_book.author} | Год: {target_book.year} | Жанр: {target_book.genre} | ISBN: {target_book.isbn}")

    def find_by_author(self, author_name):
        return [b for b in self.books if b.author is author_name]

    def find_by_genre(self, genre):
        return self.by_genre[genre]

    def find_by_year(self, year):
        return self.by_year[year]

    def find_by_isbn(self, isbn):
        result = self.by_isbn[isbn]
        return result[0] if result else None
