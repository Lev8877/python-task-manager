dollars = 80
euro = 90
uani = 11

money = float(input("Введите сумму в рублях: "))
if money < 0: 
    print("Чилсо не может быть отрицательным")
else:
    print(f"{money:.2f} рублей - это: \n{money/dollars:.2f} долларов \n{money/euro:.2f} евро \n{money/uani:.2f} юаней")