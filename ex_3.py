import math
import random

def get_input_numbers(count=1):
    res = []

    for x in range(count):
        res.append(input(f'Введите число номер {x+1}: '))

    return res

is_active = True

while is_active:
    print('Список доступных операторов: +,-,*,/,^,module,f,arccos')
    operator = input('Введите оператор или 0 для выхода: ')

    if operator == '+':
        [num1, num2] = get_input_numbers(2)
        result = int(num2) + int(num2)
        print(f'{num1}+{num2}={result}')
    elif operator == '-':
        [num1, num2] = get_input_numbers(2)
        result = int(num1) - int(num2)
        print(f'{num1}-{num2}={result}')
    elif operator == '*':
        [num1, num2] = get_input_numbers(2)
        result = int(num1) * int(num2)
        print(f'{num1}*{num2}={result}')
    elif operator == '/':
        [num1, num2] = get_input_numbers(2)
        if int(num2) == 0:
            print('На ноль делить нельзя')
        else:
            result = int(num1) / int(num2)
            print(f'{num1}/{num2}={result}')
    elif operator == '^':
        [num1, num2] = get_input_numbers(2)
        result = pow(int(num1), int(num2))
        print(f'{num1}^{num2}={result}')
    elif operator == 'module':
        [num] = get_input_numbers()
        print(abs(float(num)))
    elif operator == 'f':
        [num] = get_input_numbers()
        print(math.factorial(int(num)))
    elif operator == 'arccos':
        [num] = get_input_numbers()
        print(math.acos(int(num) * math.pi / 180))
    elif operator == '0':
        is_active = False
    else:
        print(f'Оператор {operator} не найден, будет выведенно рандомное число')
        print(f'Рандомное число: {random.randint(0, 999)}')