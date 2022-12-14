"""
切片 方法适用于 字符串、列表、元组
切片 使用 索引值 来限定范围，从一个大的字符串中切出小的字符串
列表 和 元组 都是 有序 的集合，都能够通过索引值 获取到对应的数据
字典 是一个 无序 的集合，是使用 键值对 保存数据 所有不能切片
"""

# 字符串[开始索引:结束索引:步长]
# 顺序索引：0 1 2 3 4 5 6 7 8 9
# 逆序索引：-1 -2 -3 -4 -5 -6 -7 -8 -9 -10
num_str = "0123456789"
print(num_str)

# 截取从2~5位置的字符串
print(num_str[2:6])  # 截取的字符串不包括结束索引位置的字符

# 截取从2~末尾的字符串
print(num_str[2:])

# 截取从开始~5的字符串
print(num_str[:6])

# 截取完整的字符串
print(num_str[:])

# 从开始位置,每隔一个字符截取字符串
print(num_str[::2])

# 从索引 1 位置,每隔一个字符截取字符串
print(num_str[1::2])

# 截取字符串末尾字符
print(num_str[-1])

# 截取从2~末尾-1的字符串
print(num_str[2:-1])

# 截取字符串末尾两个字符
print(num_str[-2:])

# 字符串的逆序
print(num_str[-1::-1])  # 步长 -1 表示从右向左切
