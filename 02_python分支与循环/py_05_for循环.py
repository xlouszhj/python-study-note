"""
for 变量 in 集合:
    
    循环体代码
else:
    没有通过 break 退出循环，循环结束后，会执行的代码
"""
# 应用场景
# 在 迭代遍历 嵌套的数据类型时,例如 一个列表包含了多个字典
# 需求：要判断某一个字典中是否存在指定的值 
# 如果存在,提示并且退出循环
# 如果不存在,在循环整体结束后,希望得到一个统一的提示

# 包含多个字典的列表
students = [
    {"name": "阿土",
     "age": 20,
     "gender": True,
     "height": 1.7,
     "weight": 75.0},
    {"name": "小美",
     "age": 19,
     "gender": False,
     "height": 1.6,
     "weight": 45.0},
]

find_name = "小美"

for stu_dict in students:

    print(stu_dict)

    # 判断当前遍历的字典中姓名是否为find_name
    if stu_dict["name"] == find_name:
        print("找到了 %s" % find_name)

        # 如果已经找到，直接退出循环，就不需要再对后续的数据进行比较
        break

else:
    print("没有找到 %s" % find_name)

print("循环结束")
