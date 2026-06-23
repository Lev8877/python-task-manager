product = {
    "name": "Ноутбук",
    "price": 85000,
    "quantity": 3,
    "category": "Электроника"
}
print("Ключи:")
for key in product:
    print(key)
print("Значения:")
for value in product.values():
    print(value)
print("Пары значения")
for key, value in product.items():
    print(f"{key}: {value}")
for key in product:
    if type(product[key]) == int:
        product[key] += 10 
print(product)