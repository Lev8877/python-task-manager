def calculate_average(*args):
    if not args:
        return 
    return sum(args) / len(args)

print(calculate_average(10, 20, 30))

def show_user(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_user(name = "Лев", grade = 5)