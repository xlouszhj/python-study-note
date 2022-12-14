# 局部变量 是在 函数内部 定义的变量，只能在函数内部使用
# 全局变量 是在 函数外部定义 的变量（没有定义在某一个函数内,所有函数内部都可以使用这个变量

# 函数执行时,需要处理变量时会:
# 首先查找 函数内部 是否存在 指定名称 的局部变量,如果有,直接使用
# 如果没有,查找 函数外部 是否存在 指定名称 的全局变量,如果有,直接使用
# 如果还没有,程序报错!

"""局部变量"""
# 局部变量 是在 函数内部 定义的变量,只能在函数内部使用
# 局部变量 在 函数执行时 才会被创建
# 函数执行结束后,函数内部的局部变量,会被系统回收
# 不同的函数,可以定义相同的名字的局部变量,但是 彼此之间 不会产生影响

"""全局变量"""
# 全局变量 是在 函数外部定义 的变量,所有函数内部都可以使用这个变量

# 在函数内部,可以 通过全局变量的 引用 获取对应的数据
# 但是,不允许直接修改全局变量的引用——使用赋值语句修改全局变量的值
# 如果在函数中需要修改全局变量，需要使用 `global` 进行声明
# 为了保证所有的函数都能够正确使用到全局变量,应该将全局变量定义在其他函数的上方
num = 10  

def demo1():

    print("demo1" + "-" * 50)
    # python中,函数内不允许直接修改全局变量的值
    # 只是定义了一个局部变量，不会修改到全局变量，只是变量名相同而已
    num = 100

    """
    如果在函数中需要修改全局变量,需要使用 `global` 进行声明
    global 关键字会告诉编译器,后面的是一个全局变量
    既然是全局变量,就不会创建局部变量
    global num
    num = 99
    """

    print(num)

def demo2():
    
    print("demo2" + "-" * 50)
    print(num)

demo1()
demo2()

print("over")
