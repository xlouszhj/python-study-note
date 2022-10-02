# 输入函数 input
# 用户输入的任何内容 Python 都认为是一个 字符串 
password = input("请输入密码：")
print(password)
print(type(password))  # 显然password是字符串类型
# 类型转换函数 int(x) float(x)
print(type(int(password)))  # 将password转换为整型
print(type(float(password)))  # 将password转换为浮点型

"""
变量输入演练 —— 超市买苹果增强版
需求:
收银员输入苹果的价格，单位：元／斤
收银员输入用户购买苹果的重量，单位：斤
计算并且输出付款金额
"""

price = input("苹果的单价：")
weight = input("苹果的重量：")
# money = price * weight  错误: 因为两个字符串之间是不能直接用乘法
money = float(price) * float(weight)

# 也可以在输入时直接转换：
# price = float(input("苹果的单价："))
# weight = float(input("苹果的重量："))
# money = price * weight 

"""
变量的格式化输出  格式化操作符：%
格式化字符串: %s-字符串； %d-有符号十进制整数 %06d表示输出的整数显示位数 不足的地方使用 0 补全
格式化字符串：%f-浮点数 %.2f表示小数点后只显示两位； %%-输出%
print("格式化字符串" % 变量1)
print("格式化字符串" % (变量1, 变量2...))
"""
print("苹果的单价是:%.2f元/斤,购买了%.2f斤,需要支付%.2f元" %(price,weight,money))
scale = 0.25
print("优惠比例：%.0f%%" %(scale*100)) # scale*100要加()否则就会输出100次scale
