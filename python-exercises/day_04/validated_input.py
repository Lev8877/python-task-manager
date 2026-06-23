while True:
    priority = int(input("Введите преоритет: "))
    if 1 <= priority <= 5:
        print(f"Приоритет принят: {priority}")
        break
    print("Некорректный приоритет. Попробуйте снова.")