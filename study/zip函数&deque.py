items = [
    1,
    2,
    3,
    4,
    5
]

item1 = [
    "a",
    "b",
    "c",
    "d",
    "a",
    "x"
]

a, b, c = [i for i in range(3)]

print(list(zip(item1, items)))
