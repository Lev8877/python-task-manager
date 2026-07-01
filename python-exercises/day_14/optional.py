def find_user(users: dict[int,str], user_id: int) -> str | None:
    for id in users:
        if id == user_id:
            return users[id]
    return None

print(find_user({
    1: "Анна",
    2: "Иван",
},2) is None)