import random
from models import EBook, PaperBook
from core import Library
from errors import LibraryError


def run_simulation(steps: int = 20, seed: int | None = None) -> None:
    if seed is not None:
        random.seed(seed)

    library = Library()
    authors = ["Лев Толстой", "Фёдор Достоевский", "Александр Пушкин", "Джордж Оруэлл", "Рэй Брэдбери"]
    genres = ["Классика", "Антиутопия", "Фантастика", "Драма"]
    titles = ["Путь домой", "Секреты кода", "Ночные тени", "В поисках истины", "Зеркала времени"]

    #1
    print("\n")
    lib1 = Library()
    lib1.add_book(
        PaperBook(title="Секреты кода", author="Джордж Оруэлл", year=2020, genre="Драма", isbn="ISBN-123", cover="Твердая"))
    lib2 = Library()
    print(f"Книг в lib1: {len(lib1.books)}")
    print(f"Книг в lib2: {len(lib2.books)}")
    input("\n")
    #

    #2
    is_ebook = random.randint(0, 1)
    common_params = {
        "title": random.choice(titles),
        "author": "Лев Толстой",
        "year": random.randint(1900, 2024),
        "genre": random.choice(genres),
        "isbn": f"ISBN-{random.randint(0, 999999)}"
    }
    if is_ebook:
        book = EBook(**common_params, file_size=random.randint(1, 100))
    else:
        book = PaperBook(**common_params, cover=random.choice(["твердой", "мягкой"]))
    library.add_book(book)
    author = input("Какого автора вы хотите найти? : ")
    result = library.find_by_author(author)
    print(f"Поиск автора {author}: найдено {len(result)} книг")
    input("\n")
    #

    #3
    for i in range(5):
        is_ebook = random.randint(0, 1)
        common_params = {
            "title": random.choice(titles),
            "author": "Лев Толстой",
            "year": 1999,
            "genre": random.choice(genres),
            "isbn": f"ISBN-{random.randint(0, 999999)}"
        }
        if is_ebook:
            book = EBook(**common_params, file_size=random.randint(1, 100))
        else:
            book = PaperBook(**common_params, cover=random.choice(["твердой", "мягкой"]))
        library.add_book(book)
    print(f"\nВсего в библиотеке {len(library.books)} книг.\n")
    print("Удаляем книги до 1999 года (вкл.)!")
    for book in library.books:
        if book.year < 2000:
            library.remove_book(book)
    print(f"\nВсего в библиотеке {len(library.books)} книг.\n")
    input("\n")
    #

    #4
    print(f"Критерии поиска: жанр - Драма и год - 2001")
    results = library.books.filter_by_criteria(genre="Драма", year=2001)
    print(f"Найдено книг: {len(results)}")
    for b in results:
        print(f" -> Найдено: {b.title} (Жанр: {b.genre}, Год: {b.year})")
    input("\n")
    #

    #5
    for step in range(1, steps):
        print("\n")
        print(f"{step}. ", end="")
        try:
            event = random.randint(1, 5)
            if event == 1:  # Добавление книги
                is_ebook = random.randint(0, 1)
                common_params = {
                    "title": random.choice(titles),
                    "author": random.choice(authors),
                    "year": random.randint(1900, 2024),
                    "genre": random.choice(genres),
                    "isbn": f"ISBN-{random.randint(0, 999999)}"
                }
                if is_ebook:
                    book = EBook(**common_params, file_size=random.randint(1, 100))
                else:
                    book = PaperBook(**common_params, cover=random.choice(["твердой", "мягкой"]))
                library.add_book(book)
            elif event == 2:  # Удаление книги
                if not library.books.is_empty():
                    all_books_list = list(library.books)
                    target = random.choice(all_books_list)
                    library.remove_book(target)
                else:
                    print("Событие: попытка удаления. Библиотека пуста.")
            elif event == 3:  # Поиск по автору
                author = random.choice(authors)
                result = library.find_by_author(author)
                print(f"Поиск автора {author}: найдено {len(result)} книг")
            elif event == 4:  # Поиск по isbn
                isbn = f"ISBN-{random.randint(0, 999999)}"
                print(f"Поиск книги {isbn}")
                result = library.find_by_isbn(isbn)
                print(f"    Результат: найдена книга {result.title}.")
            elif event == 5:  # Фильтрация
                genre = random.choice(genres)
                result = library.books.filter_by_criteria(genre=genre)
                print(f"Фильтр по жанру {genre}: найдено {len(result)} книг")
        except LibraryError as e:
            print(f"{e}")
        except Exception as e:
            print(f"{e}")
