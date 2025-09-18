import json
import os
import time
import random
from datetime import datetime


time_prompts = [
    "Сколько времени это заняло?:",
    "Как долго вы этим занимались?:",
    "Укажите продолжительность:",
    "На сколько хватило этого момента?",
    "Сколько минут вы провели за этим?",
    "Длительность активности:",
    "Засекали? Сколько минут прошло?",
    "Сколько времени ты потратил на это дело? 😉",
    "Сколько времени ушло на эту активность?",
    "Приблизительная продолжительность:",
    "Время, проведённое за этим делом:",
    "Сколько времени вы уделили этому?",
    "Оцените, сколько это заняло:",
    "Сколько минут или часов прошло с начала?",
    "Выделили на это:",
]
def menu():
    while True:
        print("""
Меню:
1. Главный отчёт
2. Добавить активность
3. Мои цели
4. Календарь дней
5. Настройки
6. Помощь
0. Выход
        """)

        try:
            choice = int(input("Выберите пункт меню (0-6): "))

            if choice == 1:
                show_report()
            elif choice == 2:
                add_activity()
            elif choice == 3:
                my_goals()
            elif choice == 4:
                calendar_days()
            elif choice == 5:
                settings()
            elif choice == 6:
                help_section()
            elif choice == 0:
                print("До встречи!")
                break
            else:
                print("❌ Неверный выбор. Пожалуйста, введите число от 0 до 6.")

        except ValueError:
            print("⚠️ Пожалуйста, введите число.")


def clear_screen():
    # Для Windows
    if os.name == 'nt':
        os.system('cls')
    # Для macOS и Linux
    else:
        os.system('clear')


# Заглушки для функций (их можно будет реализовать позже)
def show_report():
    print("📊 Здесь будет главный отчёт...")


def add_activity():
    clear_screen()
    print("➕ Добавление активности")
    print("""
    активности:
    1. Отдых
    2. Сон
    3. Работа
            """)
    akt = int(input("Выберите категорию активности (1-3): "))
    if akt == 1:
        akt = "Отдых"
    if akt == 2:
        akt = "Сон"
    if akt == 3:
        akt = "Работа"

    time_task = input(random.choice(time_prompts))
    save_activity(
        category=akt,
        duration=time_task,
        date=datetime.now().strftime("%Y-%m-%d"),
        time_today=datetime.now().strftime("%H:%M")
    )



def save_activity(category, duration, date, time_today):
    # Сначала загружаем существующие данные
    try:
        with open("activities.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # Если файла нет или он пуст — создаём новую структуру
        data = {"activities": []}

    # Добавляем новую активность
    activity = {
        "category": category,
        "duration": duration,
        "date": date,
        "time": time_today
    }
    data["activities"].append(activity)

    # Сохраняем обратно в файл
    with open("activities.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print("✅ Активность сохранена!")






def my_goals():
    print("🎯 Мои цели...")


def calendar_days():
    print("📅 Календарь дней...")


def settings():
    print("⚙️ Настройки...")


def help_section():
    print("❓ Помощь и инструкции...")


# Запуск
menu()