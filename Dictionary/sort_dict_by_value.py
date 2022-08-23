orders = {"a": 9, "c": 8, "b": 7, "d": 6}

x = orders.items()

x = sorted(orders.items(), key=lambda y: y[1])

orders = {k: v for k, v in x}

print(orders)
