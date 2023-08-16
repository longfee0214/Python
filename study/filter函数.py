"""
Python建议使用这种方式，而不是用map和filter函数
filtered1 = [item[1] for item in items]
"""

items = [
    ("P1", 10),
    ("P2", 9),
    ("P3", 11),
]
f = list(filter(lambda item: item[0] == "P1", items))
f1 = [item for item in items if item[0] == "P1"]

m = list(map(lambda item: item[1], items))
m1 = [item[1] for item in items]
print(m)
print(m1)
print(f)
print(f1)
