"""
Модуль для синхронизации репозиториев системы с помощью пакетного менеджера pacman.

Функции:
- update_system(): Синхронизирует репозитории системы.
"""

from .utils import run_command


def update_system():
    """Синхронизация репозиториев системы."""
    try:
        print("🔄 Синхронизируем репозитории системы...")
        run_command(["sudo", "pacman", "-Syy"])
        print("🎉 Синхронизация репозиториев завершена успешно!")

    except RuntimeError as e:
        print(e)
