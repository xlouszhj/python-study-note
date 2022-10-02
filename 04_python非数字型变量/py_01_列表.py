# List(列表)是 Python 中使用最频繁的数据类型,在其他语言中通常叫做 数组
# 专门用于存储一串信息
# 列表用 [] 定义,数据 之间使用 `,` 分隔
# 列表的 索引 从 `0` 开始
# 索引 就是数据在列表中的位置编号,索引又可以被称为下标
# 列表 中可以 存储不同类型的数据

name_list = ["张三", "李四", "王五"]

# 取值和索引
print(name_list[0])

# 知道数据内容,想确定数据在列表中的位置
print(name_list.index("李四"))

# 修改
name_list[0] = "zhangsan"
print(name_list[0])

# 增加
# append 方法可以向列表的末尾追加数据
name_list.append("王小二")
# insert 方法可以在列表的指定索引位置插入数据
name_list.insert(1,"小美眉")
# extend 方法可以把其他列表中的完整内容追加到当前列表的末尾
temp_list = ["孙悟空","猪八戒","沙师弟"]
name_list.extend(temp_list)
print(name_list)

# 删除
# remove 方法可以从列表中删除指定的数据 如果 zhangsan 在列表中不只出现一次,则只会删除第一个
name_list.remove("zhangsan")
# pop 方法默认可以把列表中最后一个元素删除
name_list.pop()
# pop 方法可以指定要删除元素的索引
name_list.pop(3)
print(name_list)
# clear 方法可以清空列表
# name_list.clear()
# print(name_list)

# 列表的数据统计
# len(length 长度)函数可以统计列表中元素的总数
list_len = len(name_list)
print("列表中包含了 %d 个元素" % list_len)
# count 方法可以统计列表中某一个数据出现的次数
count = name_list.count("孙悟空")
print("孙悟空出现了 %d 次" % count)

# 列表排序
num_list = [4,8,6,10,2]
# 升序
num_list.sort()  # 默认升序
print(num_list)
# 降序
num_list.sort(reverse=True)
print(num_list)
#逆序(反转)
name_list.reverse()
print(name_list)
