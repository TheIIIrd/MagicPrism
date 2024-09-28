"""
Модуль для удаления пакетов с помощью пакетного менеджера pacman.

Функции:
- remove_package(package_names): Удаляет указанные пакеты.
"""

from .utils import run_command


def remove_package(package_names):
    """Удаляет указанные пакеты с помощью пакетного менеджера pacman.

    Args:
        package_names (list): Список имен пакетов, которые необходимо удалить.

    Returns:
        None
    """
    if not package_names:
        print("❌ Названия пакетов не указаны.")
        return

    try:
        print(f"🗑 Удаляем пакеты: {', '.join(package_names)}")
        # Запуск команды pacman для удаления пакетов с указанием параметров
        run_command(["sudo", "pacman", "-Rsn", "--noconfirm"] + package_names)
        print(f"🎉 Удаление {', '.join(package_names)} завершено успешно!")

    except RuntimeError as e:
        print(f"❌ Ошибка при удалении пакетов: {e}")
