"""
Розробити функцію, котра приймає колекцію та обʼєкт функції, що приймає один аргумент.
Повернути колекцію, кожен член якої є перетвореним членом вхідної колекції.

Нотатка. Обʼєкт функції, яку передаємо вказує на функцію, котра приймає один аргумент.
Не користуватися функціями map чи filter!!!
"""


def receiver(fun, list_example):
    finish_result = []
    for each_element in list_example:
        finish_result.append(fun(each_element))
    return finish_result


def fun1(value):
    return value * 2.23213


print(receiver(fun1, [1, 2, 5, 6]))
