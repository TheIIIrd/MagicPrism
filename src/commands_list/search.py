"""
Модуль для поиска пакетов с помощью пакетного менеджера pacman.

Функции:
- search_package(package_names): Ищет указанные пакеты.
"""

from .utils import process_packages


def search_package(package_names):
    """Ищет указанные пакеты с помощью пакетного менеджера pacman.

    Args:
        package_names (list): Список имен пакетов для поиска.

    Returns:
        None
    """

    # Вызов функции для обработки пакетов с использованием команды поиска
    process_packages(["pacman", "-Ss"], package_names, "🔍 Ищем пакет:")
