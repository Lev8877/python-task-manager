def greet(name):
    return f"Привет {name}!"

name = input("Введите имя: ")
result = greet(name)
print(result) 

def square(number):
    return number**2

number = float(input("Введите число: "))
result = square(number)
print(f"Квадрат числа:{result}")

def is_even(number):
    return number % 2 == 0 

number = int(input("Введите число: "))
result = is_even(number)
print(result)