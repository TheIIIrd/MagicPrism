"""
Модуль для проверки целостности системных пакетов и пакетного менеджера.

Функции:
- repair_package(): Проверяет целостность системы и обновляет необходимые ключи и пакеты.
"""

from .utils import run_command


def repair_package():
    """Проверяет целостность системы и обновляет ключи и пакеты pacman.

    Returns:
        None
    """
    try:
        print("🛠️ Проверяет целостность системы...")

        # Обновление ключей Arch Linux
        run_command(
            ["sudo", "pacman", "-Sy", "--needed", "--noconfirm", "archlinux-keyring"]
        )

        # Обновление pacman-contrib, если это необходимо
        run_command(["sudo", "pacman", "-Su", "--noconfirm", "pacman-contrib"])

        # Обновление базы данных пакетов
        run_command(["sudo", "pacman", "-Fy"])

        # Очистка неиспользуемых версий пакетов при помощи paccache
        run_command(["sudo", "paccache", "-r"])

        print("🎉 Проверка завершена успешно!")

    except RuntimeError as e:
        print(f"❌ Ошибка при проверке целостности системы: {e}")
