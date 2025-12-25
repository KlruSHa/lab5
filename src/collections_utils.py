from errors import BookNotFoundError


class BookCollection:
    """Пользовательская коллекция книг"""

    def __init__(self, books = []):
        self._books = books

    """def __init__(self):
        self._books = []"""

    def __iter__(self):
        return iter(self._books)

    def __len__(self):
        return len(self._books)

    def __getitem__(self, index):
        result = self._books[index]
        if isinstance(index, slice):
            new_coll = BookCollection()
            new_coll._books = result
            return new_coll
        return result

    def __contains__(self, book):
        return book in self._books

    def add_book(self, book):
        self._books.append(book)

    def remove_book(self, book):
        if book not in self._books:
            book_ = getattr(book, 'title', book)
            raise BookNotFoundError(f"Не удалось удалить: книга {book_} отсутствует")
        self._books.remove(book)

    def filter_by_criteria(self, **criteria):
        """Фильтрация через пользовательскую коллекцию"""
        result = BookCollection()
        for book in self:
            if any(getattr(book, key, None) == value for key, value in criteria.items()):
                result.add_book(book)
        return result

    def is_empty(self):
        return len(self) == 0


class IndexDict:
    def __init__(self):
        self._data = {}

    def __getitem__(self, key):
        return self._data.get(key, [])

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def add_to_index(self, key, book):
        if key not in self._data:
            self._data[key] = []
        if book not in self._data[key]:
            self._data[key].append(book)

    def remove_from_index(self, key, book):
        if key in self._data:
            if book in self._data[key]:
                self._data[key].remove(book)
        if not self._data[key]:
            del self._data[key]
