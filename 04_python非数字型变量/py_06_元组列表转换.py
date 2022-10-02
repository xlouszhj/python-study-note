num_list = [1,2,3,4]
name_tuple = ("张三","李四","王五")

# 元组和列表转换
num_tuple = tuple(num_list)  # 将列表转换为元组 让列表数据不可以被修改 保护数据安全
print(type(num_tuple))
name_list = list(name_tuple)  # 将元组转换为列表
print(type(name_list))
