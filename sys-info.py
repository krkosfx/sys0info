import platform
import os
import socket
import psutil # type: ignore
import uuid
from datetime import datetime
import re
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


print("Собираю информацию...")
time.sleep(10)
clear_screen()

def get_mac_address():
    mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    return mac

def get_external_ip():
    try:
        ip = socket.gethostbyname(socket.gethostname())
        return ip
    except Exception as e:
        return f"Ошибка при получении IP: {e}"

def get_system_info():
    print("Информация о компьютере:")
    print(f"Имя компьютера: {socket.gethostname()}")
    print(f"Операционная система: {platform.system()} {platform.release()}")
    print(f"Архитектура: {platform.architecture()[0]}")
    print(f"Версия ОС: {platform.version()}")
    print(f"Имя пользователя: {os.getlogin()}")
    print(f"Процессоры: {psutil.cpu_count(logical=False)} (физических), {psutil.cpu_count()} (логических)")
    print(f"Частота процессора: {psutil.cpu_freq().current} МГц")
    print(f"Объем оперативной памяти: {psutil.virtual_memory().total / (1024 ** 3):.2f} ГБ")
    print(f"Объем доступной памяти: {psutil.virtual_memory().available / (1024 ** 3):.2f} ГБ")
    print(f"Объем диска: {psutil.disk_usage('/').total / (1024 ** 3):.2f} ГБ")
    print(f"Занято на диске: {psutil.disk_usage('/').used / (1024 ** 3):.2f} ГБ")
    print(f"Свободно на диске: {psutil.disk_usage('/').free / (1024 ** 3):.2f} ГБ")
    print(f"MAC-адрес: {get_mac_address()}")
    print(f"IP-адрес: {get_external_ip()}")
    print(f"Текущая дата и время: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Мой GitHub: https://github.com/krkosfx")
    time.sleep(100000000)

if __name__ == "__main__":
    get_system_info()
    