def read_integer():
    while True:
        try: 
            data = int(input("Введите целое число: "))
        except ValueError:
            print("Вы ввели не целое число")
        else:
            return data 

print(read_integer())

