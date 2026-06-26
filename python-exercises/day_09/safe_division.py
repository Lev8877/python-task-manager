def divide(first, second):
    if second == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return first / second 

try:
    result = divide(2,0)
except ZeroDivisionError as error:
    print(error)
else:
    print(result)