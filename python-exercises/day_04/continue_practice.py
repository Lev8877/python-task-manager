numbers = [5, -2, 8, 0, -7, 12, 3, 0, 10]

s = 0
for number in numbers:
    if number <= 0:
        continue 
    print(number)
    s += number 
    
print("Финальная сумма: ",s)