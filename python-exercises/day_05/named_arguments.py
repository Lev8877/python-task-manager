def calculate_price(price, discount=0, delivery=0):
    if not 0 <= discount <= 100:
        return None 
    return price * ((100-discount)/100) + delivery 

print(calculate_price(price=1000, discount=10, delivery=300))