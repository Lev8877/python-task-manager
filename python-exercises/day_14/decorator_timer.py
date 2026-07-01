from time import perf_counter
from functools import wraps

def measure_time(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        time1 = perf_counter()
        result = function(*args,**kwargs)
        time2 = perf_counter()
        print(f"Разница с начала и в конце: {time2 - time1}")
        return result 
    return wrapper


@measure_time
def calculate_sum(limit: int) -> int:
    return sum(range(limit))

result = calculate_sum(1_000_000)
print(result)