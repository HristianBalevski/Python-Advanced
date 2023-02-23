def shopping_cart(*args):
    my_cart = {'Soup': [], 'Pizza': [], 'Dessert': []}
    soup = 3
    pizza = 4
    dessert = 2
    iteration = 0
    output = ''

    for info in args:
        if info == 'Stop':
            if iteration == 0:
                return f"No products in the cart!"

            result = {k: v for k, v in sorted(my_cart.items(), key=lambda x: (-len(x[1]), x[0]))}
            for data in result.items():
                output += f"{data[0]}:\n"
                sort_products = sorted(data[1])
                for p in sort_products:
                    output += f" - {p}\n"

            return output

        iteration += 1
        meal = info[0]
        product = info[1]

        if meal == 'Soup' and len(my_cart[meal]) < soup and product not in my_cart[meal]:
            my_cart[meal].append(product)

        elif meal == 'Pizza' and len(my_cart[meal]) < pizza and product not in my_cart[meal]:
            my_cart[meal].append(product)

        elif meal == 'Dessert' and len(my_cart[meal]) < dessert and product not in my_cart[meal]:
            my_cart[meal].append(product)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
