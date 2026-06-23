correct_password = "python123"

for i in range (2,-1,-1):
    try_password = input("Введите пароль: ")
    if try_password == correct_password:
        print("Доступ разрешен")
        break
    if i != 0:
        print("Оставшиеся количество попыток: ",i)
else:
    print("Доступ запрещен")