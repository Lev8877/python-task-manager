from collections.abc import Iterator

def get_long_words(words: list[str], min_length: int) -> Iterator[str]:
    for word in words:
        if len(word) >= min_length:
            yield word 

words = ["Python", "Go", "JavaScript", "C"]

for word in get_long_words(words, 5):
    print(word)