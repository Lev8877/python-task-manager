this_year = 2026

name = input("Введите имя:")
year = int(input("Введите год рождения:"))

if year > this_year or this_year - year > 120 or year <= 0:
    print("Некорректный год рождения")
else:
    print(f"Привет, {name} \nТебе примерно: {this_year - year} лет. \nСовершеннолетний:{this_year - year >= 18}")