def require_positive(function):
    def wrapper(*args,**kwargs):
        if args[0] > 0:
            return function(*args,**kwargs)
        print("Число должно быть положительным")
        return None
    return wrapper


@require_positive
def calculate_square(number: int) -> int:
    return number**2

print(calculate_square(5))
print(calculate_square(-2))