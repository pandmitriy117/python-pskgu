# Сделать из функций калькулятора отдельный класс
import math
import random

class Calculator:
    def plus(self, num1, num2):
        return int(num1) + int(num2)

    def minus(self, num1, num2):
        return int(num1) - int(num2)
    
    def multiply(self, num1, num2):
        return int(num1) * int(num2)

    def div(self, num1, num2):
        if int(num2) == 0:
            return 'на 0 делить нельзя'
        else:
            return int(num1) / int(num2)

    def pow(self, num1, num2):
        return math.pow(int(num1), int(num2))

    def module(self, num1):
        return abs(float(num1))

    def rand(self):
        return random.randint(0, 999)

    def factorial(self, num1):
        return math.factorial(int(num1))

    def arccos(self, num1):
        return math.acos(int(num1) * math.pi / 180)
    
    def input(self, count=1):
        res = []

        for x in range(count):
            res.append(input(f'Введите число номер {x+1}: '))

        return res

calculator = Calculator()

is_active = True

while is_active:
    print('Список доступных операторов: +,-,*,/,^,module,f,arccos')
    operator = input('Введите оператор или 0 для выхода: ')

    if operator == '+':
        [num1, num2] = calculator.input(2)
        result = calculator.plus(num1, num2)
        print(f'{num1}+{num2}={result}')
    elif operator == '-':
        [num1, num2] = calculator.input(2)
        result = calculator.minus(num1, num2)
        print(f'{num1}-{num2}={result}')
    elif operator == '*':
        [num1, num2] = calculator.input(2)
        result = calculator.multiply(num1, num2)
        print(f'{num1}*{num2}={result}')
    elif operator == '/':
        [num1, num2] = calculator.input(2)
        result = calculator.div(num1, num2)
        print(f'{num1}/{num2}={result}')
    elif operator == '^':
        [num1, num2] = calculator.input(2)
        result = calculator.pow(num1, num2)
        print(f'{num1}^{num2}={result}')
    elif operator == 'module':
        [num] = calculator.input()
        print(calculator.module(num))
    elif operator == 'f':
        [num] = calculator.input()
        print(calculator.factorial(num))
    elif operator == 'arccos':
        [num] = calculator.input()
        print(calculator.arccos(num))
    elif operator == '0':
        is_active = False
    else:
        print(f'Оператор {operator} не найден, будет выведенно рандомное число')
        print(f'Рандомное число: {calculator.rand()}')