from collections.abc import Iterator

def combine_sequences(
    first: list[int],
    second: list[int],
) -> Iterator[int]:
    yield from first 
    yield from second 

print(list(combine_sequences([1, 2], [10, 20, 30])))