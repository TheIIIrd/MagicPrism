"""
Модуль для вывода информации о пакете с помощью пакетного менеджера pacman.

Функции:
- show_package(package_names): Выводит информацию о указанных пакетах.
"""

from .utils import process_packages


def show_package(package_names):
    """Выводит информацию о указанных пакетах с помощью пакетного менеджера pacman.

    Args:
        package_names (list): Список имен пакетов для отображения информации.

    Returns:
        None
    """

    # Вызов функции для обработки пакетов с использованием команды для отображения информации
    process_packages(["pacman", "-Qii"], package_names, "🗒️ Создаем сводку о пакете:")
