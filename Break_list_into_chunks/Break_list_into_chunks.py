my_list = [
    "geeks",
    "for",
    "geeks",
    "like",
    "geeky",
    "nerdy",
    "geek",
    "love",
    "questions",
    "words",
    "life",
]

# Yield successive n-sized
# chunks from l.
def divide_chunks(l, n):
    l1 = []
    # looping till length l
    for i in range(0, len(l), n):
        l1.append(l[i : i + n])
    return l1


# How many elements each
# list should have
n = 5

x = divide_chunks(my_list, n)
print(x)
