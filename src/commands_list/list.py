"""
Модуль для вывода списка установленных пакетов помощью пакетного менеджера pacman.

Функции:
- list_package(): Выводит список установленных пакетов.
"""

from .utils import run_command


def list_package():
    """Вывод списка установленных пакетов."""
    try:
        print("🗒️ Создаем список установленных пакетов")
        run_command(["pacman", "-Q"])

    except RuntimeError as e:
        print(e)
