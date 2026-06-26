def is_task_urgent(priority, hours, completion):
    return (
        priority == 5
        or (priority >= 4 and hours <= 2)
    ) and completion != 100

def get_status(completion):
    if completion == 0:
        return "Задача не начата"
    elif completion == 100:
        return "Задача завершена"
    else:
        return "Задача в процессе"
    
def read_command(text):
    while True:
        try:
            number = int(input(text))
        except ValueError:
            print("Введите целое число")
        else:
            return number