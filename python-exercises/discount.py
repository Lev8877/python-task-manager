price = int(input("Введите сумму: "))
totalprice = price
if price < 0:
    print("Некорректные данные")
else:
    student = int(input("Введите 1 если вы студент, иначе 0: "))
    card = int(input("Введите 1 если у вас есть карта магазина, иначе 0: "))
    skidka = 0
    print(f"Сумма до скидки: {price:.2f}")
    if price >= 10000:
        price -= totalprice*0.1
        skidka += 10
    elif price >= 5000:
        price -= totalprice*0.05
        skidka += 5
    if student:
        price -= totalprice*0.03
        skidka += 3
    if card:
        price -= totalprice*0.02
        skidka += 2
    print(f"Скидка: {skidka}%")
    print(f"Итого: {price:.2f}")
