def calculate_cart_total(discount_rate, *prices) -> float:
    total = 0
    for price in prices:
        discounted_price = price - (price * discount_rate / 100)
        total += discounted_price

    return float(total)
def filter_and_soret_products(**products):
    filtered_products = filter(lambda product: product[1] >= 100, products.items())

    sorted_products = sorted(
        filtered_products,
        key=lambda product: product[1]
    )

    return sorted_products

print(calculate_cart_total(10, 100, 200, 300))

print(filter_and_soret_products(
    laptop=2500,
    mouse=50,
    keyboard=150,
    headphones=200,
    monitor=800
))  