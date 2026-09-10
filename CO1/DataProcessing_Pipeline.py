from itertools import groupby, combinations

transactions = [
    ("Alice", "Laptop"),
    ("Alice", "Mouse"),
    ("Alice", "Keyboard"),
    ("Bob", "Phone"),
    ("Bob", "Earphones"),
    ("Bob", "Charger")
]

transactions.sort(key=lambda x: x[0])

for customer, group in groupby(transactions, key=lambda x: x[0]):
    products = tuple(product for _, product in group)

    print(customer, products)

    print("Combinations:")
    for combo in combinations(products, 2):
        print(combo)
