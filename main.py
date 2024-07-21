from datetime import datetime

from constants import BookStatus, Command
from models import Book, Library


def main():
    library = Library()
    while True:
        print("\nДоступные команды:")
        Command.print_commands()
        command_input = input("Введите номер команды: ").strip()

        try:
            command: Command = Command(int(command_input))
        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")
            continue

        if command == Command.ADD:
            title: str = input("Введите название книги: ")
            author: str = input("Введите автора книги: ")
            year: int = int(input("Введите год издания: "))
            if year > datetime.now().year:
                print("Год издания книги не может быть в будущем")
                continue
            library.add_book(title, author, year)
            print("Книга добавлена.")

        elif command == Command.REMOVE:
            book_id: str = input("Введите ID книги для удаления: ")
            if book_id not in library.list_books_id():
                print("Книги с таким ID не найдено")
                continue
            library.remove_book(book_id)
            print("Книга удалена.")

        elif command == Command.FIND:
            query: str = input(
                "Введите запрос для поиска (название, автор, год): "
            )
            found_books: list[Book] = library.find_books(query)
            if not found_books:
                print(f"Книги по запросу '{query}' не найдены")
            for book in found_books:
                print(
                    f"ID книги: {book.book_id}\n"
                    f"Название: {book.title}\n"
                    f"Автор: {book.author}\n"
                    f"Год издания: {book.year}\n"
                    f"Статус книги: {book.status}\n"
                )

        elif command == Command.LIST:
            for book in library.list_books():
                print(
                    f"ID книги: {book.book_id}\n"
                    f"Название: {book.title}\n"
                    f"Автор: {book.author}\n"
                    f"Год издания: {book.year}\n"
                    f"Статус книги: {book.status}\n"
                )

        elif command == Command.UPDATE:
            book_id = input("Введите ID книги для изменения статуса: ")
            if book_id not in library.list_books_id():
                print("Книги с таким ID не найдено")
                continue
            print("\nДоступные статусы:")
            BookStatus.print_commands()
            status_input = input("Введите номер статуса: ").strip()

            try:
                status: BookStatus = BookStatus(int(status_input))
            except ValueError:
                print("Некорректный ввод. Попробуйте снова.")
                continue
            library.update_status(book_id, status)
            print("Статус книги обновлен.")

        elif command == Command.EXIT:
            break

        else:
            print("Неизвестная команда. Попробуйте снова.")


if __name__ == "__main__":
    main()
