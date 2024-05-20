#цикл for
for value in collection:
#пример использования
    for i in range(3):
        print(i + 1, "шаг цикла")
        print("Первый цикл закончился!")
#перебор значений коллекции с помощью for
for value in [1, 2, 3, 4, 5]:
    print(value)
for value in (1, 2, 3, 4, 5):
    print(value)
for value in {1, 2, 3, 4, 5}:
    print(value)
#функция range
range(start,stop,step)
#примеры использования функции range()
range(10)
# Генерация последовательности чисел от 0 до 9
range(1, 11)
# Генерация последовательности чисел от 1 до 10
range(1, 11, 2)
# Генерация последовательности чисел от 1 до 10 с шагом 2
range(10, 0, -1)
# Генерация последовательности чисел от 10 до 1 с шагом -1
#примеры функции range()
print(range(10)) # объект типа range
print(list(range(10))) # список целых чисел от 0 до 9 включительно
print(tuple(range(1, 11))) # кортеж целых чисел от 1 до 10 включительно
print(list(range(1, 11, 2))) # список целых нечетных чисел от 1 до 9 включительно
print(tuple(range(10, 0, -1))) # range так же поддерживает отрицательный шаг
#именование переменной в цикле
for in range(5): # Просто выполнить цикл 5 раз
print("Hello World!")
#рефакторинг кода
numbers = [10, 20, 30, 40, 50]
total = 0
for i in range(len(numbers)):
    total += numbers[i]
print('Сумма чисел:', total)

for num in numbers:
    total += num

#использование функции enumerate в Python
for tuple_ in enumerate(["а", "б", "в"]):
print(tuple_)

#функция enumerate в Python
for pos, value in enumerate('абв', start=1):
    print('Позиция:', pos, '->', 'Значение:', value)

#цикл while
count = 0
while count < 5:
    print('Значение count:', count)
    count += 1

sum_ = 0
input_number = int(input("Введите число: "))
while input_number != 0:
    sum_ += input_number
    input_number = int(input("Введите число: "))
print('Ответ:', sum_)


