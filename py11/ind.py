#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import datetime


def main():
    humans = []
    while True:
        command = get_command()
        if command == 'exit':
            break

        elif command == 'add':
            humans.append(add())
            if len(humans) > 1:
                humans.sort(key=lambda item: item.get('name'))

        elif command == 'list':
            print_list(humans)

        elif command.startswith('select'):
            select(command, humans)

        elif command == 'help':
            print_help()
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


def get_command():
    return input(">>> ").lower()


def add():
    name = input("Фамилия и имя: ")
    tel = input("Номер телефона: ")
    dateString = input("День рождения: ")
    human = {
        'name': name,
        'tel': tel,
        'date': datetime.strptime(dateString, "%Y-%m-%d")
    }
    return human


def print_list(humans):
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 16
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^16} |'.format(
            "No",
            "Ф.И.",
            "Телефон",
            "Дата рождения"
        )
    )
    print(line)
    for idx, human in enumerate(humans, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>16} |'.format(
                idx,
                human.get('name', ''),
                human.get('tel', ''),
                human.get('date', 0)
            )
        )
    print(line)

def select(command, humans):
    parts = command.split(' ', maxsplit=1)
    period = int(parts[1])
    count = 0
    for human in humans:
        if human['date'].month == period:
            count += 1
            print(
                '{:>4}: {}'.format(count, human.get('name', ''))
            )
    if count == 0:
        print("В этом месяце ни у кого нет дня рождения.")

def print_help():
    print("Список команд:\n")
    print("add - добавить человека;")
    print("list - вывести список людей;")
    print("select <месяц> - месяц рождения человека/людей;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")


if __name__ == '__main__':
    main()
