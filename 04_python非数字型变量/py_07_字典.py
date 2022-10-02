"""
`dictionary`(字典)是 除列表以外 `Python`之中最灵活的数据类型
字典同样可以用来 存储多个数据
   通常用于存储描述一个`物体`的相关信息
和列表的区别
   列表 是 有序 的对象集合
   字典 是 无序 的对象集合
 字典用 `{}` 定义
 字典使用 键值对 存储数据，键值对之间使用 `,` 分隔
    键 `key` 是索引
    值 `value` 是数据
    键 和 值 之间使用 `:` 分隔
    键必须是唯一的
    值 可以取任何数据类型,但 键 只能使用 字符串、数字 或 元组
"""

# 字典是一个无序的数据集合,使用print函数输出字典时，输出的顺序可能和定义的顺序是不一致的！
xiaoming_dict = {"name": "小明",  # 此处 key值 使用字符串,也可以使用数字或元组
            "age": 18,
            "gender": True,
            "height": 1.75,
            "weight": 75.5}
print(xiaoming_dict)

# 取值
print(xiaoming_dict["name"])
# print(xiaoming_dict.get("name"))  # 同上 但key不存在也不会报错

# 增加/修改
# 如果key不存在,会新增键值对
xiaoming_dict["girlfriend"] = False
# 如果key已存在,会修改已经存在的键值对
xiaoming_dict["name"] = "单身狗"
# 如果key存在,也不会修改键值对,如果key不存在,新增键值对
# xiaoming_dict.setdefault(key,value)
print(xiaoming_dict)

# 删除指定键值对
# del xiaoming_dict[key]
xiaoming_dict.pop("girlfriend")  # 注意小括号里的是key
# xiaoming_dict.popitem()  # 随机删除一个键值对
print(xiaoming_dict)

# 统计键值对数量
print(len(xiaoming_dict))

# 合并字典
temp_dict = {"age": 20,
             "phone": 123456789}
# 注意：如果被合并的字典中包含以及存在的键值对，会覆盖原有的键值对
xiaoming_dict.update(temp_dict)
print(xiaoming_dict)

# 查询所有key
print(xiaoming_dict.keys())

# 查询所有values
print(xiaoming_dict.values())

# 查询所有(key,values)
print(xiaoming_dict.items())

# 清空字典
xiaoming_dict.clear()
print(xiaoming_dict)
