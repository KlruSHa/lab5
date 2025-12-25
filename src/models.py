from abc import ABC, abstractmethod
from datetime import datetime
from errors import ValidationError


class Book(ABC):
    """Абстрактный класс для всех книг"""

    def __init__(self, title, author, year, genre, isbn, **kwargs):
        cur_year = datetime.now().year
        if not (0 < year <= cur_year):
            raise ValidationError(f"Некорректный год: {year}")
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn
        super().__init__(**kwargs)

    @abstractmethod
    def get_info(self):
        pass

    def __repr__(self):
        return f"[{self.__class__.__name__}] {self.author} - {self.title} ({self.year})"


class EBook(Book):
    def __init__(self, file_size, eformat="PDF", **kwargs):
        super().__init__(**kwargs)
        self.file_size = file_size
        self.eformat = eformat

    def get_info(self):
        return f"Электронная книга {self.title} с разрешением {self.eformat} и размером {self.file_size} MB"


class PaperBook(Book):
    def __init__(self, cover="твердой", **kwargs):
        super().__init__(**kwargs)
        self.cover = cover

    def get_info(self):
        return f"Бумажная книга {self.title} с {self.cover} обложкой"
