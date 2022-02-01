#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def positive():
    print("Число положительное")


def negative():
    print("Число отрицтаельное")


def test():
    number = int(input("Введите целое число: "))
    if number > 0:
        positive()
    elif number < 0:
        negative()
    else:
        print("Число - 0")


if __name__ == '__main__':
    test()
