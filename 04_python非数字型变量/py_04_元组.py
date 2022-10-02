# `Tuple`(元组)与列表类似,不同之处在于元组的 元素不能修改
# 元组 表示多个元素(可以不同数据类型)组成的序列
# 元组 在`Python`开发中,有特定的应用场景
# 用于存储一串信息,数据之间使用`,`分隔
# 元组用`()`定义
# 元组的索引从`0`开始
# 索引 就是数据在 元组 中的位置编号

info_tuple = ("张三",18,1.75)

# 元组索引与列表一样
print(info_tuple[0])

# 元组的 元素不能修改
# info_tuple[0] = "李四"  # 错误 会报错

# 定义空元组
empty_tuple = ()

# 元组中只包含一个元素时,需要在元素后面添加逗号
single_tuple = (5)  # 错误 它的类型是int
print(type(single_tuple))
single_tuple1 = (5,)  # 正确 
print(type(single_tuple1))

# 取索引
print(info_tuple.index("张三"))

# 统计计数
count = info_tuple.count("张三")
print("张三在元组中出现的次数：%d " % count)
# 统计元组包含元素个数
print(len(info_tuple))

# 在开发中,元组更多的应用场景是：
# 函数的 参数 和 返回值，一个函数可以接收 任意多个参数，或者 一次返回多个数据
# 有关 函数的参数 和 返回值，在后续 函数高级 给大家介绍
# 格式字符串，格式化字符串后面的`()`本质上就是一个元组
print("%s 年龄是 %d 身高是 %.2f" % info_tuple)
# 让列表不可以被修改，以保护数据安全

