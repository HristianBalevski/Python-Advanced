def shopping_list(budget, **kwargs):
    if budget < 100:
        return 'You do not have enough budget.'

    bought_products = []

    for product, value in kwargs.items():
        price = value[0]
        quantity = value[1]

        total_price = price * quantity

        if budget >= total_price:
            bought_products.append(f"You bought {product} for {total_price:.2f} leva.")
            budget -= total_price

        if len(bought_products) == 5:
            break
    return '\n'.join(bought_products)
