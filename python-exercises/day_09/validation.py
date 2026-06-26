def validate_percentage(value):
    if not 0 <= value <= 100:
        raise ValueError("Число не входит в диапазон процентов")
    return value

try: 
    result = validate_percentage(101)
except ValueError as error:
    print(error)
else:
    print(result)

