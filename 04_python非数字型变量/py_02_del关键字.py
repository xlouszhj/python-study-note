name_list = ["张三","李四","王五"]

# 使用 del 关键字(delete)删除列表元素
del name_list[1]
print(name_list)

# del 关键字本质上是用来将一个变量从内存中删除的
name = "小明"

del name

# 显示错误 变量 name 未定义
print(name) 
