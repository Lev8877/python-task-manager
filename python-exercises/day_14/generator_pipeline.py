from collections.abc import Iterator

def generate_numbers(limit: int) -> Iterator[int]:
    for number in range(limit):
        yield number 

def get_squares(numbers: Iterator[int]) -> Iterator[int]:
    for number in numbers:
        yield number**2 


generator = get_squares(generate_numbers(5))
print(list(generator))
