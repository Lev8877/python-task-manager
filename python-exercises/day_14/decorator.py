def log_call(function):
    def wrapper(*args,**kwargs):
        print("Функция запущена")
        result = function(*args,**kwargs)
        print("Функция завершена")
        
        return result
        
    return wrapper

@log_call
def greet(name: str) -> str:
    return f"Привет, {name}"

print(greet("Лев"))