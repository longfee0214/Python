from sys import getsizeof

point = {"x": 1,
         "y": 2}
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20
print(point)
print(point.get("a", 0))  # 获取a的值，如果获取不到返回0
del point["x"]
print(point)
for key, value in point.items():  # 字典迭代输出
    print(key, value)

values = {str(x): x * 2 for x in range(5)}
print(values)

# 迭代器对象和列表的使用,迭代器没有len
values = (x * 2 for x in range(1000))
print("字节数:", getsizeof(values))
values = [x * 2 for x in range(1000)]
print("字节数:", getsizeof(values))

# 练习
# 找到下面字符串使用频率最高的一个字母
sentence = "This is a common interview question"
temp_dist = {}
for i in sentence:
    if i not in temp_dist:
        temp_dist[i] = 1
    else:
        temp_dist[i] += 1
print(temp_dist)
char_frequency_sorted = sorted(temp_dist.items(),
                               key=lambda kv: kv[1],
                               reverse=True)
print(char_frequency_sorted[0])
print(f"使用最多的字母是{char_frequency_sorted[0][0]},使用了{char_frequency_sorted[0][1]}次")
