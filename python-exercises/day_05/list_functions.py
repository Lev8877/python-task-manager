def get_positive_numbers(numbers):
    result = []
    for i in numbers:
        if i > 0:
            result.append(i)
    return result 

def calculate_average(numbers):
    if not numbers:
        return None 
    return sum(numbers)/len(numbers)

def find_maximum(numbers):
    if not numbers:
        return None
    maximum = numbers[0]
    for i in numbers:
        if maximum < i:
            maximum = i 
    return maximum

number = [1,2,3,4,5,-1,-2,-3]

print(get_positive_numbers(number))
print(calculate_average(number))
print(find_maximum(number))