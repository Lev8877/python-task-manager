numbers = [3, 5, 3, 8, 5, 10, 8, 12]
set_numbers = set(numbers)

print(numbers)
print(*set_numbers)
print(len(set_numbers))
print("Есть ли число 10?: ",10 in set_numbers)
print("Отсутствует ли число 7?: ",7 not in set_numbers)
print(sorted(set_numbers))