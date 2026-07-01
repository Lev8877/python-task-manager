from collections.abc import Iterator

def generate_ids(start: int = 0) -> Iterator[int]:
    while True:
        start += 1
        yield start 

gen = generate_ids()
for _ in range(5):
    print(next(gen))