user = {
    "name": "Лев",
    "age": 20,
    "city": "Москва",
    "is_student": True
}

print(user["name"])
print(user.get("age"))
print(user.get("Слабость","Сила"))
user["city"] = "Королёв"
print(user)
user["university"] = "Misis"
print(user)
user.pop("is_student")
print(user)
print(*user.keys())
print(*user.values())
for key, value in user.items():
    print(key, value)
print("Ключ age есть в user?: ","age" in user)
user2 = user.copy()
user2.clear()
print(user)
print(user2)
