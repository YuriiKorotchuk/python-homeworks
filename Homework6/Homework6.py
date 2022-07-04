# Hапишіть программу "Касир в кінотеатрі", яка буде виконувати наступне:
# Попросіть користувача ввести свій вік.
# - якщо користувачу менше 7 - вивести "Тобі ж <>! Де твої батьки?"
# - якщо користувачу менше 16 - вивести "Тобі лише <>, а це є фільм для дорослих!"
# - якщо користувачу більше 65 - вивести "Вам <>? Покажіть пенсійне посвідчення!"
# - якщо вік користувача складається з однакових цифр (11, 22, 44 і тд років, всі можливі варіанти!) -
# вивести "О, вам <>! Який цікавий вік!"
# - у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <>, білетів всеодно нема!"
# Замість <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік
# Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача.
# Наприклад :
# "Тобі ж 5 років! Де твої батьки?"
# "Вам 81 рік? Покажіть пенсійне посвідчення!"
# "О, вам 33 роки! Який цікавий вік!"
# Зробіть все за допомогою функцій! Для кожної функції пропишіть докстрінг або тайпхінтінг.
# Не забувайте що кожна функція має виконувати тільки одну завдання і про правила написання коду.
# P.S. Для цієї і для всіх наступних домашок пишіть в функціях докстрінги або хінтінг
from termcolor import colored
from tqdm import tqdm
import time



def year_parameterize(years):
    """
    This function returns the correct type of "age[рік] word"
    :param years: the different types of age word
    :type: str
    :return: correct word type
    """
    if years[-1] == "1" and years[-2:] != "11":
        return "рік"
    elif years[-1] == "2" and years[-2:] != "12":
        return "роки"
    elif years[-1] == "3" and years[-2:] != "13":  # Міг помістити все в один еліф, але не хотів виходити за рамки :)
        return "роки"
    elif years[-1] == "4" and years[-2:] != "14":
        return "роки"
    else:
        return "років"


def movie_viewer(customer):
    """
    This function contains logic + validation for the viewer year exercise
    :param customer: the result from the age input
    :type: str
    :return: correct option from print part
    """
    for i in tqdm(range(5)):
        time.sleep(0.3)
    years_old = year_parameterize(customer)
    if not customer.isnumeric():
        print("Поле повинно містити тільки цифри!")
    elif customer.startswith("0"):
        print("Вік не повинен починатись з 0!!!")
    else:
        valid_year = int(customer)
        if valid_year < 7:
            print(f"Тобі ж {customer} {years_old}! Де твої батьки?")
        elif customer.count(customer[0]) == len(customer) and len(customer) > 1:
            print(f"О, вам {customer} {years_old}! Який цікавий вік!")
        elif valid_year < 16:
            print(f"Тобі лише {customer} {years_old}, а це є фільм для дорослих!")
        elif valid_year > 65:
            print(f"Вам {customer} {years_old}? Покажіть пенсійне посвідчення!")
        else:
            print(f"Незважаючи на те, що вам {customer} {years_old}, білетів всеодно нема!")


viewer_year = input(colored("Скільки вам років??? ", 'green', attrs=['blink'])) # закоментуйте перед запуском пайтестів
movie_viewer(viewer_year) # закоментуйте перед запуском пайтестів








