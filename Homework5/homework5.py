# Task 1 - Напишіть функцію, що приймає один аргумент.
# Функція має вивести на екран тип цього аргумента (для визначення типу використайте type)
import pyfiglet as pyg


def type_receiver(type_data):
    print(pyg.figlet_format(str(type(type_data)), font="digital"))


type_receiver(1)


# Task 2: Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент,
# перетворений на float. Якщо перетворити не вдається функція має повернути 0 (флоатовий нуль).

def float_transformator(content):
    try:
        if type(content) == float or type(content) == int or type(content) == str:
            return float(content)
    except ValueError as e:
        return 0.0
    else:
        return 0.0


# Task 3: Напишіть функцію, що приймає два аргументи. Функція повинна
# якщо аргументи відносяться до числових типів - повернути різницю цих аргументів,
# якщо обидва аргументи це строки - обʼєднати в одну строку та повернути
# якщо перший строка, а другий ні - повернути dict де ключ це перший аргумент, а значення - другий
# у будь-якому іншому випадку повернути кортеж з цих аргументів

def math_examples(firstly, secondary):
    if (type(firstly) == int or type(firstly) == float) and (type(secondary) == int or type(secondary) == float):
        return firstly - secondary
    elif (type(firstly)) == str and (type(secondary)) == str:
        return firstly + secondary
    elif (type(firstly)) == str and (type(secondary)) != str:
        return {firstly: secondary}
    else:
        return firstly, secondary
