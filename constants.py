from enum import Enum, auto

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
