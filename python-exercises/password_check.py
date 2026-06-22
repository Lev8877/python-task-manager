login = input()
password = input()
nn = True
if len(password) < 8:
    print("Пароль слишком короткий")
    nn = False 
if login == password:
    print("Пароль не должен совпадать с именем")
    nn = False 
if password == "password" or password == "12345678":
    print("Слишком простой пароль")
    nn = False 
if nn == True:
    print("Надежный пароль")