age = int(input())
if age < 0 or age > 120:
    print("Некорректный возраст")
elif age <= 6:
    print("ребёнок")
elif 7 <= age <= 17:
    print("школьник")
elif 18 <= age <= 24:
    print("молодой человек")
elif 25 <= age <= 59:
    print("взрослый")
else:
    print("пожилой человек")