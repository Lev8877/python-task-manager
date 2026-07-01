def log_arguments(function):
    def wrapper(*args,**kwargs):
        print("Позиционные:")
        for i in args:
            print(i)
            
        print("Именованные:")
        for key, value in kwargs.items():
            print(f"{key}: {value}")
        print("Основная функция:")
        result = function(*args,**kwargs)
        return result

    return wrapper 


@log_arguments
def create_user(name: str, age: int, active: bool = True) -> dict:
    return {
        "name": name,
        "age": age,
        "active": active,
    }


user = create_user("Лев", 20, active=False)
print(user)