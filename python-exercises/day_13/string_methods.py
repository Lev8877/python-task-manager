from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: int

    def __str__(self):
        return f"{self.name} - {self.price} Р"
    

product = Product("Ноутбук",10000)

print(product)
print(repr(product))