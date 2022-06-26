# Task 2 - Є два довільних числа які відповідають за мінімальну і максимальну ціну.
# Є Dict з назвами магазинів і цінами: { "cilpio": 47.999, "a_studio" 42.999, "momo": 49.999, "main-service":
# 37.245, "buy.ua": 38.324, "my-store": 37.166, "the_partner": 38.988, "sto": 37.720, "rozetka": 38.003}.
# Напишіть код, який знайде і виведе на екран назви магазинів, ціни яких попадають в діапазон між мінімальною
# і максимальною ціною. Наприклад:
# lower_limit = 35.9
# upper_limit = 37.339
# > match: "my-store", "main-service"

my_dict = {"cilpio": 47.999,
           "a_studio": 42.999,
           "momo": 49.999,
           "main-service": 37.245,
           "buy.ua": 38.324,
           "my-store": 37.166,
           "the_partner": 38.988,
           "sto": 37.720,
           "rozetka": 38.003,
           }

achievements_list = []

try:
    lower_limit = float(input("Введіть мінімальну ціну: "))
    upper_limit = float(input("Введіть максимальну ціну: "))
except ValueError as e:
    print("Ви написали не валідне значення!!!")
else:
    if lower_limit > upper_limit:
        print("Ціна нижнього ліміту не повинна бути більша чим ціна верхнього!!!")
    else:
        for shop, price in my_dict.items():
            if lower_limit <= price <= upper_limit:
                achievements_list.append(shop)
    if len(achievements_list) < 1:
        print("Результатів за данною фільтрацією не знайдено!!!")
    else:
        print(f"Список магазинів за данною фільтрацією: {achievements_list}")