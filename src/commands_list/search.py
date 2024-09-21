"""
Модуль для поиска пакетов с помощью пакетного менеджера pacman.

Функции:
- search_package(package_name): Ищет указанный пакет.
"""


def search_package(package_name):
    """Поиск указанного пакета (пока заглушка)."""
    if not package_name:
        print("❌ Название пакета не указано.")
        return

    try:
        print(f"🔍 Ищем пакет: {package_name}")
        run_command(["pacman", "-Ss", package_name])

    except RuntimeError as e:
        print(e)
