products = [
    {"name": "Клавиатура", "price": 5000, "available": True},
    {"name": "Мышь", "price": 2500, "available": False},
    {"name": "Монитор", "price": 30000, "available": True},
]

def find_product(products, name):
    if not products:
        return
    for product in products:
        if name == product["name"]:
            return f"Товар найден, его цена {product['price']}"
    return "Товар не найден"
    
def get_available_products(products):
    if not products:
        return
    result = []
    for product in products:
        if product["available"] == 1:
            result.append(product["name"])
    return result 

def find_cheapest_available_product(products):
    if not products:
        return
    minimum = None
    for product in products:
        if product["available"] == 1 and (minimum == None or product["price"] < minimum):
            minimum = product["price"]
    return minimum 

print(find_product(products, "Клавиатура"))
print(*get_available_products(products))
print(f"Товар с минимальной ценой: {find_cheapest_available_product(products)}")