# 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
player = int(input("请出拳 石头(1)/剪刀(2)/布(3):"))

# 电脑 随机 出拳 
import random  # 要使用随机数，首先需要导入随机数的模块
computer = random.randint(1,3)  # 返回[a, b]之间的整数，包含a和b 下限必须小于上限

# 比较胜负
# 逻辑运算符包括：与 and／或 or／非 not 三种
if ((player == 1 and computer == 2) or
        (player == 2 and computer == 3) or
        (player == 3 and computer == 1)):
        # 注意 冒号：不能少
        # 如果条件判断的内容太长，可以在最外侧的条件增加一对大括号
        # 再在每一个条件之间，使用回车，PyCharm 可以自动增加 8 个空格
    print("噢耶！！！电脑弱爆了！！！")  
    # 代码的缩进为一个tab键或者4个空格 
    # 缩进了才是if满足条件后要执行的语句，不缩进则不管if条件是否满足都会执行
    # 可以将 if、elif 和 else 以及各自缩进的代码，看成一个完整的代码块
elif player == computer:  # elif的应用场景是：同时判断多个条件，所有的条件是平级的
    print("心有灵犀，再来一盘！")
else:
    print("不行，我要和你决战到天亮！")
