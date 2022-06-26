# Task 3 Існує ліст з різними даними, наприклад
# lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть механізм, який сформує новий list (наприклад lst2), який би містив всі числові змінні, які є в lst1.
# Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.

from rich import print

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = lst1.copy()

for i in lst1:
    if type(i) != int and type(i) != float:
        lst2.remove(i)
print(lst1)
print(f"List #2: :Ukraine: {lst2} :Ukraine:")

