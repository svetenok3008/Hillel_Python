# Напишіть програму, яка запитує у користувача рік і перевіряє, чи він
# високосний. Рік високосний, якщо він ділиться на 4 без залишку, але не
# ділиться на 100 без залишку, за винятком років, які діляться на 400 без
# залишку. Виведіть відповідне повідомлення на екран за допомогою print.

# Приклад:
# Введіть рік: 2024
# Рік є високосним.

year = int(input('Input year: '))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"The {year} is leap")
else:
    print(f"The {year} isn't leap")
