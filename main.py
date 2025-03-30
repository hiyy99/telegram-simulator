# -*- coding: utf-8 -*-
import json

def load_json(file_name):
    """Загружает JSON из файла"""
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Файл не найден.")
        return []
    except json.JSONDecodeError:
        print("Ошибка в структуре JSON.")
        return []

def save_json(file_name, data):
    """Сохраняет данные в JSON файл"""
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def view_messages(data):
    """Просмотр сообщений"""
    if data:
        print("Список сообщений:")
        for item in data:
            print(f"ID: {item['id']} | Сообщение: {item['message']} | Время: {item['timestamp']}")
    else:
        print("Нет сообщений для отображения.")

def add_message(data):
    """Добавление нового сообщения"""
    message = input("Введите текст сообщения: ")
    timestamp = input("Введите дату и время сообщения (формат: YYYY-MM-DD HH:MM:SS): ")
    new_message = {
        "id": len(data) + 1,
        "message": message,
        "timestamp": timestamp
    }
    data.append(new_message)
    print("Сообщение успешно добавлено.")
    return data

def find_message_by_id(data):
    """Поиск сообщения по ID"""
    try:
        search_id = int(input("Введите ID сообщения: "))
        message = next((item for item in data if item['id'] == search_id), None)
        if message:
            print(f"Сообщение найдено: ID: {message['id']} | {message['message']} | {message['timestamp']}")
        else:
            print("Сообщение с указанным ID не найдено.")
    except ValueError:
        print("Ошибка: ID должно быть числом.")

def filter_messages_by_keyword(data):
    """Фильтрация сообщений по ключевому слову"""
    keyword = input("Введите ключевое слово для поиска: ").lower()
    filtered = [item for item in data if keyword in item['message'].lower()]
    if filtered:
        print(f"Сообщения, содержащие '{keyword}':")
        for item in filtered:
            print(f"ID: {item['id']} | Сообщение: {item['message']} | Время: {item['timestamp']}")
    else:
        print(f"Нет сообщений, содержащих '{keyword}'.")

def main():
    print("Запуск Telegram Simulator...")
    file_name = 'data.json'
    data = load_json(file_name)
    
    while True:
        print("\nМеню:")
        print("1. Просмотр сообщений")
        print("2. Добавить сообщение")
        print("3. Найти сообщение по ID")
        print("4. Фильтрация сообщений по ключевому слову")
        print("5. Выйти")
        
        choice = input("Выберите действие (1-5): ")
        
        if choice == '1':
            view_messages(data)
        elif choice == '2':
            data = add_message(data)
            save_json(file_name, data)
        elif choice == '3':
            find_message_by_id(data)
        elif choice == '4':
            filter_messages_by_keyword(data)
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
