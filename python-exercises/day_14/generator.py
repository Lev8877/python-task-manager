def generate_even_numbers(limit: int):
    for number in range(limit):
        if number % 2 == 0:
            yield number 

for even_number in generate_even_numbers(10):
    print(even_number)