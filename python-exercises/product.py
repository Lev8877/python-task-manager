product = {}

name = input("Введите название продукта: ")
product["name"] = name 
price = float(input("Введите цену продукта: "))
quantity = int(input("Введите количество продукта: "))
if price < 0 or quantity < 0:
    print ("Неверные данные")
else:
    product["price"] = price 
    product["quantity"] = quantity
    category = input("Введите категорию продукта: ")
    product["category"] = category
    product["total_price"] = price * quantity
    product["is_available"] = quantity > 0 
    product["is_expensive"] = price>10000
    print(product)
