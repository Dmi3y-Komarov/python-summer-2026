import os
import json
from datetime import datetime

FILE_NAME = "notes.json"

#print(os.name)

def load_notes():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_notes(notes):
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        json.dump(notes, f, ensure_ascii=False, indent=4)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_note():
    clear_console()
    print('==} Режим добавления заметки {==')
    print('Введите текст заметки. Пустая строка - выход из режима')
    
    text = input('Текст: ').strip()

    if not text:
        print('Добавление отменено')
        return

    notes = load_notes()

    new_id = 1 if not notes else max(note['id'] for note in notes) + 1

    new_note = {
            'id' : new_id,
            'text' : text,
            'date' : datetime.now().strftime("%Y-%m-%d %H.%M")
            }
    notes.append(new_note)
    print('Успешно добавлено')
    save_notes(notes)
    input('\nPress Enter to return in menu')

def show_all_notes():
    clear_console()
    notes = load_notes()
    if not notes:
        print('Nothing to see here')
    else:
        print('All notes:\n')
        for note in notes:
            print(f'[{note["id"]}] (note["date"]): {note["text"]}')
    
    input('\nPress Enter to return in menu')

def show_one():
    clear_console()
    notes = load_notes()
    if not notes:
        print('Nothing to see here')
        input('\nPress Enter to escape in menu')
        return

    print('Чтение по одной заметке, Enter - следующая, "q" - выход:\n')

    for note in notes:
        clear_console()
        print(f'---Заметка #{note["id"]} дата: {note["date"]}')
        print(note["text"])

        user_input = input('Нажмите Enter для следующей или "q" для выхода').strip().lower()
        if user_input=='q':
            break
    print('\nPress Enter to go in menu')

def delete_note():
    clear_console()
    notes = load_notes()
    if not notes:
        print('Nothing to see here')
        input('Press Enter to return in menu')
        return

    print('Режим удаления')
    for note in notes:
        print(f'#{note["id"]} ({note["date"]}):\n{note["text"]}')

    try:
        id_to_delete =int(input('Введите id для удаления(0 для отмены): '))
        if id_to_delete==0:
            print('Press Enter to go in menu')
            return

        for i, note in enumerate(notes):
            if note["id"]==id_to_delete:
                delete_note = notes.pop(i)
                save_notes(notes)
                print(f'Заметка (delete_note["text"]) удалена!')
                break
        else:
            print('Заметки с таким id не существует')

    except ValueError:
        print('Ошибка: нужно ввести число')

    input('\nPress Enter to return in menu')

def main_menu():
    while True:
        clear_console()
        print("======} notes.py {======")
        choice = int(input("1) Добавить заметку\n2) Показать все\n3) Читать по одной\n4) Удалить заметку\n0) Выход\n"))
        
        if choice==1:
            add_note()
        elif choice==2:
            show_all_notes()
        elif choice==3:
            show_one()
        elif choice==4:
            delete_note()
        elif choice==0:
            print('Goodbye!')
            break
        else:
            print('Неверный ввод. Попробуйте ещё раз!')
            input('Press Enter....')

#============= main =============
if __name__=="__main__":
    main_menu()
