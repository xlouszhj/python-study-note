# 变量的定义和类型
"""
数据类型 可以分为 数字型 和 非数字型
数字型:
   整型 (int)
   浮点型(float)
   布尔型(bool) 
      真  True (非0数) —— 非零即真
      假  False (0)
   复数型 (`complex`)
      主要用于科学计算，例如：平面场问题、波动问题、电感电容等问题
非数字型:
   字符串
   列表
   元组
   字典
"""

# 姓名：小明     (字符串string)
name = "小明"

# 年龄：18岁   （整型int）
age = 18

#性别：是男生   （布尔型bool）
gender = True  # T必须大写

# 身高：1.75 米  （浮点型float）
height = 1.75

# 体重：75.0公斤   
weight = 75.0  # (浮点型float)

# 使用 `type` 函数可以查看一个变量的类型
type(name)

# 字符串变量 之间使用 '+' 拼接字符串
first_name = "张"
last_name = "三"
first_name + last_name  # '张三'

# 字符串变量 可以和 整数 使用 `*` 重复拼接相同的字符串
"-" * 5  # '-----'

# 数字型变量 和 字符串 之间 不能进行其他计算
# age + name  错误

