"""
1、Python的值类型和引用类型
    这是Python中值类型（如整数、浮点数、字符串等）和引用类型（如列表、字典、类的实例等）的一个重要区别。
    值类型在赋值操作时会创建一个新的副本，而引用类型在赋值操作时只会创建一个新的引用。
    例如：
        items = [
        ("P1", 10),
        ("P2", 9),
        ("P3", 11),
        ]
        items1 = items
    如果items被修改，items1也跟着被修改
2、map和lambda的使用：
    lambda相当于传参一个函数，函数使用该参数return一个表达式
        例如：
            def sum（a）:
                return a*a
            和
            (lambda a: a*a)(4)  输出16，代表将4执行a*a
            a   为函数的传参
            a*a 为要执行的命令
            4   为传入的参数
    map函数接受一个函数和一个可迭代对象作为参数，然后对可迭代对象中的每个元素应用这个函数
        例如：
            numbers = [1, 2, 3, 4, 5]
            squares = map(lambda x: x ** 2, numbers)
            print(list(squares))  # 输出：[1, 4, 9, 16, 25]
            
            map函数：第一个参数是要对第二个参数执行的动作
            第二个参数是一个可迭代对象
            返回一个对象
    filter函数

"""


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5, 6))

# 倒序输出列表
a = list(range(20))
print(a[::-1])
# 列表多个赋值
a = [1, 2, 3, 4, 5, 6, 7]
first, second, *other, last = a
print(f"first:{first} second:{second} last:{last} other:{other}")
# enumerate枚举对象
for index, letter in enumerate(a):
    print(f"index:{index} letter:{letter}")
# lambda使用
items = [
    ("P1", 10),
    ("P2", 9),
    ("P3", 11),
]
items1 = items.copy()
items.sort(key=lambda item: item[1])
print(items)
# map的使用
prices = list(map(lambda item: item[1], items1))
print(f"prices: {prices}")

print((lambda b: (b * b))(4))
