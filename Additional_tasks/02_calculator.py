# Давайте створимо простий калькулятор. Напишіть програму, яка запитує у
# користувача два цілих числа і виконує такі дії:
# - обчислює суму та виводить результат.
# - обчислює різницю і виводить результат (перше число мінус друге число).
# - обчислює добуток та виводить результат.
# - обчислює ділення (результат поділу першого числа на друге) та виводить
#   результат.
# - обчислює залишок від поділу першого числа на друге та виводить результат.
# - Зводить перше число у ступінь другого числа та виводить результат.
import math
num_1 = int(input('Input the first number: '))
num_2 = int(input('Input the second number: '))
print("The result of summation is: ", num_1 + num_2)
print("The result of difference is: ", num_1 - num_2)
print("The result of multiplication is: ", num_1 * num_2)
print("The result of deviation is: ", num_1 / num_2)
print("The rest of deviation is: ", num_1 // num_2)
print(f"The {num_1} in {num_2} is: ", num_1 ** num_2)