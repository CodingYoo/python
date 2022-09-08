# 字符串 String
var1 = "123"
print(var1)
print(var1[:1])

# 数字 Number
var2 = 123.001
print(var2)

# 列表 List ：元素可修改
var3 = [1, 2, 3]
print(var3)

# Tuple（元组）：元素不可修改
var4 = (1, 2, 3, 4)
print(var4)

"""
string、list 和 tuple 都属于 sequence(序列)。
"""

# Set(集合)：无序,重复元素自动去掉
var5 = {"212", 1, 3, 5, 5, 1}
print(var5)

# Dictionary(字典) : key:value;key不可重复;创建空字典{}
var6 = {'name': 'python', "age": 10, 'site': 'www.python.org'}
print(var6['age'])
