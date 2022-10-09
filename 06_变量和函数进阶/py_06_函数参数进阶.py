"""
无论传递的参数是 可变 还是 不可变 
只要针对 参数 使用 赋值语句,会在 函数内部 修改 局部变量 的引用,不会影响到 外部变量的引用
"""

def demo(num, num_list):
    
    print("函数内部")

    # 赋值语句
    num = 200
    num_list = [1, 2, 3]

    print(num)
    print(num_list)

    print("函数代码完成")


gl_num = 99
gl_list = [4, 5, 6]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)


"""
如果传递的参数是 可变类型,在函数内部使用 方法 修改了数据的内容,同样会影响到外部的数据
"""
def mutable(num_list):
    
    # num_list = [1, 2, 3]
    num_list.extend([1, 2, 3])  # 使用 方法 修改数据内容
    
    print(num_list)

gl_list = [6, 7, 8]
mutable(gl_list)
print(gl_list)


"""
面试题 +=
在`python`中,列表变量调用 `+=` 本质上是在执行列表变量的`extend`方法,不会修改变量的引用
"""

def demo(num, num_list):
    
    print("函数内部代码")

    num += num  
    # num = num + num
    # 仅改变局部变量的值,不会改变外部的全局变量
    num_list += num_list
    # 本质上是: num_list.extend(num_list) 由于是调用方法,所以不会修改变量的引用
    # 函数执行结束后,外部数据同样会发生变化

    print(num)
    print(num_list)
    print("函数代码完成")

gl_num = 9
gl_list = [1, 2, 3]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)   