# 有时可能需要 一个函数 能够处理的参数 个数 是不确定的,这个时候就可以使用 多值参数
# `python`中有 两种 多值参数：
# 参数名前增加 一个 `*` 可以接收 元组
# 参数名前增加 两个 `*` 可以接收 字典
# 一般在给多值参数命名时,习惯使用以下两个名字
# `*args` —— 存放 元组 参数,前面有一个 `*`
# `**kwargs` —— 存放 字典 参数,前面有两个 `*`
# `args` 是 `arguments` 的缩写,有变量的含义
# `kw` 是 `keyword` 的缩写,`kwargs`可以记忆 键值对参数

"""举例"""
def demo(num, *args, **kwargs):
    
    print(num)
    print(args)
    print(kwargs)

demo(1, 2, 3, 4, 5, name="小明", age=18, gender=True)


"""多值参数案例 —— 计算任意多个数字的和"""
# 定义一个函数 `sum_numbers`,可以接收的 任意多个整数
# 功能要求：将传递的 所有数字累加 并且返回累加结果

def sum_numbers(*args):  # *args 存放元组参数,如果不加'*',直接传一个元组进来,则要求调用时要加上小括号表明传入的是一个元组
    
    num = 0
    # 遍历 args 元组顺序求和
    for n in args:
        num += n

    return num

print(sum_numbers(1, 2, 3))  


""" 
元组和字典的拆包:
    在调用带有多值参数的函数时,如果希望：
    将一个 元组变量 ,直接传递给 `args`
    将一个 字典变量 ,直接传递给 `kwargs`
    就可以使用 拆包 ,简化参数的传递, 拆包 的方式是：
    在 元组变量前,增加 一个 `*`
    在 字典变量前,增加 两个 `*`
"""

def demo(*args, **kwargs):
    
    print(args)
    print(kwargs)


# 需要将一个元组变量/字典变量传递给函数对应的参数
gl_nums = (1, 2, 3)
gl_xiaoming = {"name": "小明", "age": 18}

# demo(gl_nums, gl_xiaoming)
# 会把元组 gl_nums 和字典 gl_xiaoming 作为一个元组传递给 args

# 拆包语法:
demo(*gl_nums, **gl_xiaoming)
# 把元组 gl_nums 传递给 args; 把字典 gl_xiaoming 传递给 kwargs