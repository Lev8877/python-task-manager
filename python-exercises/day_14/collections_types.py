def get_positive_numbers(numbers: list[int]) -> list[int]:
    return [i for i in numbers if i > 0]

def count_words(words: list[str]) -> dict[str,int]:
    result: dict[str,int] = {}

    for word in words:
        result[word] = result.setdefault(word,0) + 1 
        
    return result
