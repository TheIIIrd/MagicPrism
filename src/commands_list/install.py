"""
Модуль для установки пакетов с помощью пакетного менеджера pacman.

Функции:
- install_package(package_names): Устанавливает указанные пакеты.
"""

from .utils import run_command


def install_package(package_names):
    """Устанавливает указанные пакеты с помощью пакетного менеджера pacman.

    Args:
        package_names (list): Список имен пакетов, которые необходимо установить.

    Returns:
        None
    """
    if not package_names:
        print("❌ Названия пакетов не указаны.")
        return

    try:
        print(f"📦 Устанавливаем пакеты: {', '.join(package_names)}")
        # Запуск команды pacman для установки пакетов
        run_command(["sudo", "pacman", "-Sy", "--noconfirm"] + package_names)
        print(f"🎉 Установка {', '.join(package_names)} завершена успешно!")

    except RuntimeError as e:
        print(f"❌ Ошибка при установке пакетов: {e}")
