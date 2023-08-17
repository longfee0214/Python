# 计算函数运行使用时间, 使用timeit模块
from timeit import timeit

aa = """
try:
    # age = int(input("input age: "))
    age = 0
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("Error input")
else:
    print("No except thrown")
finally:
    print("finally 无论异不异常都会执行")
"""

bb = """
def ca(age):
    if age <= 0:
        return None
    return 10/age

x = ca(-1)
if x == None:
    pass
"""
# print(timeit(aa, number=1000))
print(timeit(bb, number=1000))
