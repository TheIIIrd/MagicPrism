"""
Модуль для удаления пакетов с помощью пакетного менеджера pacman.

Функции:
- remove_package(package_name): Удаляет указанный пакет.
"""

from .utils import run_command


def remove_package(package_name):
    """Удаление указанного пакета."""
    if not package_name:
        print("❌ Название пакета не указано.")
        return

    try:
        print(f"🗑 Удаляем пакет: {package_name}")
        run_command(["sudo", "pacman", "-Rsn", "--noconfirm", package_name])
        print(f"🎉 Удаление {package_name} завершено успешно!")

    except RuntimeError as e:
        print(e)
