def create_message(name, greeting="Привет", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"

print(create_message("Лев"))
print(create_message("Анна", "Доброе утро"))
print(create_message("Иван", punctuation="."))