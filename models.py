import json
import uuid


class Book:
    def __init__(
            self,
            title: str,
            author: str,
            year: int,
            status: str = "в наличии",
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
    def __init__(self, filepath='library.json'):
        self.filepath = filepath
        self.books = self.load_books()

    def load_books(self) -> list[Book]:
        try:
            with open(self.filepath, 'r') as file:
                books_data = json.load(file)
                return [Book(**book) for book in books_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_books(self):
        """Сохранение книг в файл в формате json."""
        with open(self.filepath, 'w') as file:
            json.dump(
                [book.to_dict() for book in self.books],
                file,
                ensure_ascii=False,
                indent=4
            )

    def add_book(self, title, author, year):
        """Добавление книги."""
        new_book = Book(title=title, author=author, year=year)
        self.books.append(new_book)
        self.save_books()

    def remove_book(self, book_id):
        """Удаление книги."""
        self.books = [book for book in self.books if book.book_id != book_id]
        self.save_books()

    def find_books(self, search_query: str) -> list[Book]:
        """Поиск книги по автору, названию или году."""
        found_books = [book for book in self.books if
                       search_query.lower() in book.title.lower() or
                       search_query.lower() in book.author.lower() or
                       search_query == str(book.year)]
        return found_books

    def list_books(self) -> list[Book]:
        """Получение списка всех книг"""
        return self.books

    def update_status(self, book_id, status):
        """Изменение статуса книги."""
        for book in self.books:
            if book.book_id == book_id:
                book.status = status
