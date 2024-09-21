"""
Модуль для обновления пакетов системы с помощью пакетного менеджера pacman.

Функции:
- upgrade_system(): Обновляет пакеты системы.
"""

from .utils import run_command


def upgrade_system():
    """Обновление пакетов системы."""
    try:
        print("🔄 Обновляем установленные пакеты...")
        run_command(["sudo", "pacman", "-Syu"])
        print("🎉 Обновление пакетов системы завершено успешно!")

    except RuntimeError as e:
        print(e)
