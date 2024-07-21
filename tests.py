import json
from typing import List

from constants import BookStatus
from models import Book, Library

filepath = 'test_app.json'

# Очищаем файл с тестовыми данными
open(filepath, 'w').close()

library = Library(filepath=filepath)


def get_books_from_file() -> list[Book]:
    """Получение списка книг из файла."""
    with open(filepath, 'r') as file:
        try:
            books_data = json.load(file)
            books_data = [Book(**book) for book in books_data]
        except (FileNotFoundError, json.JSONDecodeError):
            print("Ошибка в ходе чтения файла")
    return books_data


def add_new_book(
        title: str = 'Shining',
        author: str = "Stephen King",
        year: int = 1977
) -> dict[str:str | int]:
    """Добавление книги в библиотеку."""
    library.add_book(title, author, year)
    return {'title': title, 'author': author, 'year': year}


def test_the_book_was_added():
    """Проверка добавления новой книги в библиотеку."""
    new_added_book: dict[str:str | int] = add_new_book()
    book_from_file: Book = get_books_from_file()[0]
    if all(
            [
                book_from_file.title == new_added_book['title'],
                book_from_file.author == new_added_book['author'],
                book_from_file.year == new_added_book['year']
            ]
    ):
        print("ПРОЙДЕН")
    else:
        print("НЕ ПРОЙДЕН")


def test_update_book_status():
    """Проверка обновления статуса книги."""
    book_from_file: Book = get_books_from_file()[0]
    library.update_status(book_from_file.book_id, BookStatus.ISSUED)
    book_from_file: Book = get_books_from_file()[0]
    if book_from_file.status == 'Выдана':
        print("ПРОЙДЕН")
    else:
        print("НЕ ПРОЙДЕН")


def test_find_book_by_title():
    """Проверка поиска книги по названию."""
    # Добавляем еще 1 книги в библиотеку
    add_new_book(
        title="The Hitchhiker's Guide to the Galaxy",
        author='Douglas Noel Adams',
        year=1978
    )
    find_book: list[Book] = library.find_books('Guide to the Galaxy')
    if all(
            [
                len(find_book) == 1,
                find_book[0].title == "The Hitchhiker's Guide to the Galaxy",
                find_book[0].author == "Douglas Noel Adams",
                find_book[0].year == 1978
            ]
    ):
        print("ПРОЙДЕН")
    else:
        print("НЕ ПРОЙДЕН")


def test_not_find_book_by_title():
    """Проверка поиска книги по названию, которого нет в библиотеки."""
    title: str = 'Not Shining'
    find_book: list[Book] = library.find_books(title)
    if not find_book:
        print("ПРОЙДЕН")
    else:
        print("НЕ ПРОЙДЕН")


def test_get_books_list():
    """Проверка на получение списка книг в библиотеке."""
    books_in_library: list[Book] = library.list_books()
    if all(
            [
                len(books_in_library) == 2,
                books_in_library[0].title == 'Shining',
                books_in_library[0].author == "Stephen King",
                books_in_library[0].year == 1977,
                books_in_library[1].title == "The Hitchhiker's "
                                             "Guide to the Galaxy",
                books_in_library[1].author == "Douglas Noel Adams",
                books_in_library[1].year == 1978,
            ]
    ):
        print("ПРОЙДЕН")
    else:
        print("НЕ ПРОЙДЕН")


def test_book_delete():
    """Проверка удаления книги."""
    books_from_file: list[Book] = get_books_from_file()
    library.remove_book(books_from_file[0].book_id)
    library.remove_book(books_from_file[1].book_id)
    book_from_file: list[Book] = get_books_from_file()
    if not book_from_file:
        print("ПРОЙДЕН")
    else:
        print("НЕ ПРОЙДЕН")


if __name__ == '__main__':
    print("Тест на добавление книги в библиотеку:")
    test_the_book_was_added()
    print("Тест на изменения статуса книги:")
    test_update_book_status()
    print("Тест на поиск книги по названию:")
    test_find_book_by_title()
    print("Тест на поиск книги по названию, которого нет в библиотеке:")
    test_not_find_book_by_title()
    print("Тест на получение списка книг:")
    test_get_books_list()
    print("Тест на удаление книг из библиотеки:")
    test_book_delete()
