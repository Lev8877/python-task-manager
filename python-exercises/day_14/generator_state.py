from collections.abc import Iterator

def countdown(start: int) -> Iterator[int]:
    for number in range(start,-1,-1):
        yield number 

timer = countdown(3)

print(next(timer))
print(next(timer))

for number in timer:
    print(number)