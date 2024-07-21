from enum import auto, Enum


class Command(Enum):
    """Доступные команды."""

    ADD = auto()
    REMOVE = auto()
    FIND = auto()
    LIST = auto()
    UPDATE = auto()
    EXIT = auto()

    def __str__(self):
        """Добавляем перевод действий для отображения пользователю."""
        descriptions = {
            "ADD": "Добавить",
            "REMOVE": "Удалить",
            "FIND": "Найти",
            "LIST": "Список",
            "UPDATE": "Изменить",
            "EXIT": "Выход"
        }
        return f"{self.value} - {descriptions[self.name]}"

    @staticmethod
    def print_commands():
        """Отображение списка команд."""
        for command in Command:
            print(str(command))


class BookStatus(Enum):
    """Доступные статусы книг."""
    ISSUED = 0
    INSTOCK = 1

    def __str__(self):
        """Добавляем перевод статусов для отображения пользователю."""
        descriptions = {
            "INSTOCK": "В наличии",
            "ISSUED": "Выдана",
        }
        return f"{self.value} - {descriptions[self.name]}"

    @staticmethod
    def print_commands():
        """Отображение списка доступных статусов."""
        for status in BookStatus:
            print(str(status))
