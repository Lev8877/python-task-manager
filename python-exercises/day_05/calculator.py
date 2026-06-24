def add(a, b):
    return a + b 

def subtract(a, b):
    return a - b 

def multiply(a, b):
    return a * b 

def divide(a, b):
    if b == 0:
        return None
    else:
        return a / b 

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
print("+  -  *  /")
arithmetic_sign = input("Выберите какую арифмитическую операцию хотите выполнить(вставте знак): ")

if arithmetic_sign == "+":
    print(add(a,b))
elif arithmetic_sign == "-":
    print(subtract(a,b))
elif arithmetic_sign == "*":
    print(multiply(a,b))
elif arithmetic_sign == "/":
    result = divide(a, b)

    if result is None:
        print("Деление на ноль невозможно")
    else:
        print(result)
else:
    print("Неизвестная операция")