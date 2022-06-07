# задача номер 3 на функциях

import math
import random

def get_input_numbers(count=1):
    res = []

    for x in range(count):
        res.append(input(f'Введите число номер {x+1}: '))

    return res

def plus(num1, num2):
    return int(num1) + int(num2)

def minus(num1, num2):
    return int(num1) - int(num2)

def multiply(num1, num2):
    return int(num1) * int(num2)

def div(num1, num2):
    if int(num2) == 0:
        return 'на 0 делить нельзя'
    else:
        return int(num1) / int(num2)

def _pow(num1, num2):
    return math.pow(int(num1), int(num2))

def module(num1):
    return abs(float(num1))

def rand():
    return random.randint(0, 999)

def factorial(num1):
    return math.factorial(int(num1))

def arccos(num1):
    return math.acos(int(num1) * math.pi / 180)

is_active = True

while is_active:
    print('Список доступных операторов: +,-,*,/,^,module,f,arccos')
    operator = input('Введите оператор или 0 для выхода: ')

    if operator == '+':
        [num1, num2] = get_input_numbers(2)
        result = plus(num1, num2)
        print(f'{num1}+{num2}={result}')
    elif operator == '-':
        [num1, num2] = get_input_numbers(2)
        result = minus(num1, num2)
        print(f'{num1}-{num2}={result}')
    elif operator == '*':
        [num1, num2] = get_input_numbers(2)
        result = multiply(num1, num2)
        print(f'{num1}*{num2}={result}')
    elif operator == '/':
        [num1, num2] = get_input_numbers(2)
        result = div(num1, num2)
        print(f'{num1}/{num2}={result}')
    elif operator == '^':
        [num1, num2] = get_input_numbers(2)
        result = _pow(num1, num2)
        print(f'{num1}^{num2}={result}')
    elif operator == 'module':
        [num] = get_input_numbers()
        print(module(num))
    elif operator == 'f':
        [num] = get_input_numbers()
        print(factorial(num))
    elif operator == 'arccos':
        [num] = get_input_numbers()
        print(arccos(num))
    elif operator == '0':
        is_active = False
    else:
        print(f'Оператор {operator} не найден, будет выведенно рандомное число')
        print(f'Рандомное число: {rand()}')