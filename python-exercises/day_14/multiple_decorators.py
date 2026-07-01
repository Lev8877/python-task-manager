def make_upper(function):
    def wrapper(*args,**kwargs):
        result = function(*args,**kwargs).upper()
        return result 
    return wrapper 

def add_brackets(function):
    def wrapper(*args,**kwargs):
        result = "[" + function(*args,**kwargs) + "]"
        return result 
    return wrapper 

@add_brackets
@make_upper
def get_message() -> str:
    return "hello"

print(get_message())