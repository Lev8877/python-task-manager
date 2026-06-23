numbers = [12, -5, 7, 0, 18, -3, 4, 21, 0]
s = 0
positive = 0
negative = 0
count_0 = 0
s_even = 0
maximum = numbers[0]
minimum = numbers[0]

for i in numbers:
    s += i
    if i > 0:
        positive += 1
    if i < 0:
        negative += 1
    if i == 0:
        count_0 += 1
    if i % 2 == 0:
        s_even += i 
    if i > maximum:
        maximum = i 
    if i < minimum:
        minimum = i 

print(f"Сумма всех чисел: {s}")
print(f"Положительных чисел: {positive}")
print(f"Отрицательных чисел: {negative}")
print(f"Количество нулей: {count_0}")
print(f"Сумма чётных чисел: {s_even}")
print(f"Максимальное число: {maximum}")
print(f"Минимальное число: {minimum}")