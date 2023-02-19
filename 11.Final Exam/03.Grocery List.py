def shop_from_grocery_list(budget, shopping_list, *store):
    my_order = {}

    for data in store:
        product_name = data[0]
        price = data[1]

        if budget < price or len(shopping_list) == 0:
            break

        if product_name in shopping_list:
            if product_name not in my_order:
                my_order[product_name] = price
                budget -= price
                shopping_list.remove(product_name)

    if len(shopping_list) == 0:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(shopping_list)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
