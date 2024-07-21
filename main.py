from constants import Command
from models import Library


def main():
    library = Library()
    while True:
        print("\nДоступные команды:")
        Command.print_commands()
        command_input = input("Введите номер команды: ").strip()

        try:
            command = Command(int(command_input))
        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")
            continue

        if command == Command.ADD:
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания: "))
            library.add_book(title, author, year)
            print("Книга добавлена.")

        elif command == Command.REMOVE:
            book_id = input("Введите ID книги для удаления: ")
            library.remove_book(book_id)
            print("Книга удалена.")

        elif command == Command.FIND:
            query = input("Введите запрос для поиска (название, автор, год): ")
            found_books = library.find_books(query)
            for book in found_books:
                print(f"{book.id} - {book.title}, {book.author}, {book.year}, {book.status}")

        elif command == Command.LIST:
            for book in library.list_books():
                print(f"{book.id} - {book.title}, {book.author}, {book.year}, {book.status}")

        elif command == Command.UPDATE:
            book_id = input("Введите ID книги для изменения статуса: ")
            status = input("Введите новый статус (в наличии, выдана): ")
            library.update_status(book_id, status)
            print("Статус книги обновлен.")

        elif command == Command.EXIT:
            break

        else:
            print("Неизвестная команда. Попробуйте снова.")

if __name__ == "__main__":
    main()
