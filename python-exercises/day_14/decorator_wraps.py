from functools import wraps

def log_call(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        print("Функция запущена")
        result = function(*args,**kwargs)
        print("Функция завершена")
        
        return result
        
    return wrapper

@log_call
def greet(name: str) -> str:
    """Возвращает приветствие."""
    return f"Привет, {name}"


print(greet.__name__)
print(greet.__doc__)