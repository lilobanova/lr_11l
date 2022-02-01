#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import datetime


def main():
    workers = []
    while True:
        command = get_command()
        if command == 'exit':
            break

        elif command == 'add':
            workers.append(add())
            if len(workers) > 1:
                workers.sort(key=lambda item: item.get('name'))

        elif command == 'list':
            print_list(workers)

        elif command.startswith('select'):
            select(command, workers)

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
    worker = {
        'name': name,
        'tel': tel,
        'date': datetime.strptime(dateString, "%Y-%m-%d")
    }
    return worker


def print_list(workers):
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
    for idx, worker in enumerate(workers, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>16} |'.format(
                idx,
                worker.get('name', ''),
                worker.get('tel', ''),
                worker.get('date', 0)
            )
        )
    print(line)

def select(command, workers):
    parts = command.split(' ', maxsplit=1)
    period = int(parts[1])
    count = 0
    for worker in workers:
        if worker['date'].month == period:
            count += 1
            print(
                '{:>4}: {}'.format(count, worker.get('name', ''))
            )
    if count == 0:
        print("В этом месяце ни у одного из работников нет дня рождения.")

def print_help():
    print("Список команд:\n")
    print("add - добавить работника;")
    print("list - вывести список работников;")
    print("select <месяц> - месяц рождения работника;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")


if __name__ == '__main__':
    main()
