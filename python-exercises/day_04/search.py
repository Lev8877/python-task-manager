users = ["anna", "lev", "ivan", "maria", "alex"]

name = input("Введите имя пользователя: ")
for i in users:
    if name == i:
        print("Пользователь найден")
        break 
else:
    print("Пользователь не найден")