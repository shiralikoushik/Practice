"""Sort the values of first list using second list in Python"""


def sort_list(a, b):
    c = zip(b, a)
    for _, x in sorted(c):
        print(x)


sort_list(
    ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"],
    [0, 1, 1, 0, 1, 2, 2, 0, 1],
)
