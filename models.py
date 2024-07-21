import json
import uuid

from constants import BookStatus


class Book:
    """Класс книг."""

    def __init__(
            self,
            title: str,
            author: str,
            year: int,
            status: str = "В наличии",
            book_id: str | None = None
    ):
        self.title = title
        self.author = author
        self.year = year
        self.status = status
        self.book_id = book_id or str(uuid.uuid4())

    def to_dict(self) -> dict:
        """Преобразование объекта класса в словарь."""
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
            "book_id": self.book_id
        }


class Library:
    """Класс библиотеки для хранения и обработки книг."""

    def __init__(self, filepath='library.json'):
        self.filepath = filepath
        self.books = self.load_books()

    def load_books(self) -> dict[str: Book]:
        """
        Загрузка книг из файла. Храним данные в виде словаря, где ключами
        являются book_id. Это нужно для быстрого поиска книг по book_id.
        """
        try:
            with open(self.filepath, 'r') as file:
                books_data = json.load(file)
                return {book['book_id']: Book(**book) for book in books_data}
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_books(self) -> None:
        """Сохранение книг в файл в формате json."""
        with open(self.filepath, 'w') as file:
            json.dump(
                [book.to_dict() for book in self.books.values()],
                file,
                ensure_ascii=False,
                indent=4
            )

    def add_book(self, title: str, author: str, year: int) -> None:
        """Добавление книги."""
        new_book: Book = Book(title=title, author=author, year=year)
        self.books[new_book.book_id] = new_book
        self.save_books()

    def remove_book(self, book_id) -> None:
        """Удаление книги."""
        self.books.pop(book_id)
        self.save_books()

    def find_books(self, search_query: str) -> list[Book]:
        """Поиск книги по автору, названию или году."""
        found_books = [book for book in self.books.values() if
                       search_query.lower() in book.title.lower() or
                       search_query.lower() in book.author.lower() or
                       search_query == str(book.year)]
        return found_books

    def list_books(self) -> list[Book]:
        """Получение списка всех книг."""
        return list(self.books.values())

    def list_books_id(self) -> list[str]:
        """Получение списка ID всех книг."""
        return list(self.books.keys())

    def update_status(self, book_id: str, status: BookStatus) -> None:
        """Изменение статуса книги."""
        if book_id in self.books:
            new_status: str = "Выдана" if status == BookStatus.ISSUED \
                else "В наличии"
            self.books[book_id].status = new_status
        self.save_books()
