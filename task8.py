a, s, p = 1, 150, 200
while a <= 10:
    a += 2
    p += a
    s += p
print(f'Переменная s={s}')

a, s, p = 1, 150, 200
while True:
    if a > 10:
        break
    a += 2
    p += a
    s += p
print(f'Переменная s={s}')

s = 1
for i in range(1,6):
    s *= n
print('Конец алгоритма')
print(f'Переменная s = {s}')

m,n = 12,5
