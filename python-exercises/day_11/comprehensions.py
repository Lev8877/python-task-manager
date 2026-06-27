numbers = [-5, -2, 0, 3, 4, 7, 10]

print([i**2 for i in numbers])
print([i for i in numbers if i > 0])
print([i**2 for i in numbers if i % 2 == 0])
print({i:"Четное" if i % 2 == 0 else "Нечетное" for i in numbers})