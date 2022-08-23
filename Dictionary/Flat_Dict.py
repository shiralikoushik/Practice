dict1 = {"name": ["Jan", "Feb", "March"], "month": [1, 2, 3]}
x = [value for value in dict1.values()]

y = {key: value for key, value in zip(x[1], x[0])}

print(y)
