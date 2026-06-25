def is_even(number):
    return number % 2 == 0 

def get_square(number):
    return number**2 

def get_larger(first, second):
    return first if first > second else second 

if __name__ == "__main__":
    print(is_even(2))
    print(get_square(10))
    print(get_larger(2,3))