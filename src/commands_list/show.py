"""
Модуль для вывода информации о пакете с помощью пакетного менеджера pacman.

Функции:
- show_package(package_names): Выводит информацию о пакете.
"""

from .utils import process_packages


def show_package(package_names):
    """Вывод информации о пакете."""
    process_packages(["pacman", "-Qii"], package_names, "🗒️ Создаем сводку о пакете:")
