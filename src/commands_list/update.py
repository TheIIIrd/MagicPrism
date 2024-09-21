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
        run_command(["pacman", "-Syy"])
        print(f"🎉 Синхронизация репозиториев завершено успешно!")

    except RuntimeError as e:
        print(e)
