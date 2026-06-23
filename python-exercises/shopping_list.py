shopping_list = ["морковь","салат","помидор","кола"]

new = input().strip().lower()
if not new:
    print("Товар не может быть пустым")
else:
    if new not in shopping_list:
        shopping_list.append(new)
    delete = input().strip().lower()
    if delete in shopping_list:
        shopping_list.remove(delete)
    else:
        print("Такого товара нет в списке")
    print(f"Список: {shopping_list} \nКоличество товаров: {len(shopping_list)}")