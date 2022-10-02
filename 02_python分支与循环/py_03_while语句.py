# 计算 0 ~ 100 之间 所有偶数的累计求和结果
# 0. 定义一个变量储存结果
result = 0
# 1. 计数器
i = 0
# 2. 开始循环
# while语句以及缩进部分(缩进4个空格或者一个Tab）是一个完整的代码块
while i <= 100:  
    # 判断偶数
    if i % 2 == 0:
        print(i)
        result += i
    # 处理计数器 不能忘记这点否则会陷入死循环
    i += 1
print("0~100之间偶数求和结果 = %d" %result)

# break和continue
"""
break 某一条件满足时,退出循环,不再执行后续重复的代码
continue 某一条件满足时,不执行后续重复的代码,进行下一次循环
"""
i = 0
while i < 10:
    # break 某一条件满足时，退出循环，不再执行后续重复的代码
    # i == 3
    if i == 3:
        break
        # 结果应为 0 1 2 
    print(i)
    i += 1
print("over")

i = 0
while i < 10:
    # 当 i == 7 时，不希望执行需要重复执行的代码
    if i == 7:
        # 在使用 continue 之前，同样应该修改计数器
        # 否则会出现死循环
        i += 1
        continue
    # 重复执行的代码
    # 结果不会打印出7
    print(i)
    i += 1
