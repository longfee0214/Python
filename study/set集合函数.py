numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}
print(first | second)  # 两个集合所有包含的
print(first - second)  # 第一个集合比第二个集合多余的数
print(first & second)  # 集合相同点
print(first ^ second)  # 集合不同点

values = {x * 2 for x in range(5)}
print(values)
"""
集合没有index，想要使用index先转换成list

因为集合是无序的
"""
