correct_login = "admin"
correct_password = "python123"
correct_code = 7777

login = input()
password = input()
code = int(input())

if login != correct_login:
    print("Неверный логин")
elif password != correct_password:
    print("Неверный пароль")
elif code != correct_code:
    print("Неверный код")
else:
    print("Доступ разрешен")