from functools import wraps 

def repeat(times: int):
    def decorator(function):
        @wraps(function)
        def wrapper(*args,**kwargs):
            for _ in range(times):
                function(*args,**kwargs)
        return wrapper
    return decorator


@repeat(3)
def show_message(message: str) -> None:
    print(message)


show_message("Python")