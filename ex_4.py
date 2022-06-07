vegetables = []

# Вводим 3 произвольных слова, например, название овощей.
for i in range(3):
    vegetables.append(input(f'Введите овощ номер {i + 1}: '))

# Выводим все 3 слова в нижнем регистре и в верхнем
print('== Выводим все 3 слова в нижнем регистре: ==')
for vegetable in vegetables:
    print(vegetable.lower())

print('== В верхнем регистре ==')
for vegetable in vegetables:
    print(vegetable.upper())

print('== Потом только первый символ в верхнем (есть отдельная функция для этого). ==')

for vegetable in vegetables:
    print(vegetable.title())

# Далее вводим кол-во каждого овоща.
vegetableList = {}
for vegetable in vegetables:
    vegetableList[vegetable] = input(f'Введите количество {vegetable}: ')

for vegetable in vegetables:
    print('{}: {}шт'.format(vegetable, vegetableList[vegetable]))