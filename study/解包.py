# 列表解包
# numbers = list(range(5)) 等价于下面解包
numbers = [*range(5), *"Hello"]
print(*numbers)
print(numbers)

# 字典解包
# 具有相同的键的值以最后一个解包的为准
first = {"x": 1}
second = {"y": 2, "z": 3, "x": 10}
combined = {**first, **second}
print(combined)
