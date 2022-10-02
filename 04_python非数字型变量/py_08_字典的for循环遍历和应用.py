xiaoming_dict = {"name":"小明",
                 "age": 18,
                 "height": 1.75}

# 迭代遍历字典
# 变量 k 是每一次循环中,获取到的键值对的key
for k in xiaoming_dict:
    print("%s - %s" %(k , xiaoming_dict[k]))
 
print('-' * 80) 
"""
在开发中,字典更多的应用场景是：
  使用 多个键值对,存储 描述一个`物体`的相关信息 —— 描述更复杂的数据信息
  将 多个字典 放在 一个列表 中,再进行遍历,在循环体内部针对每一个字典进行 相同的处理
"""
card_list = [
    {"name": "张三",
     "qq": "123456",
     "phone": "110"},
    {"name": "李四",
     "qq": "654321",
     "phone": "911"}
]

for card_info in card_list:
    print(card_info)
