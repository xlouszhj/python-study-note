# 定义函数时,可以给 某个参数 指定一个 默认值,具有默认值的参数就叫做 缺省参数
# 调用函数时,如果没有传入 缺省参数 的值，则在函数内部使用定义函数时指定的 参数默认值
# 函数的缺省参数,将常见的值设置为参数的缺省值,从而 简化函数的调用

# 例如：对列表排序的方法
gl_num_list = [6, 3, 9]

# 默认就是升序排序，因为这种应用需求更多
gl_num_list.sort()
print(gl_num_list)

# 只有当需要降序排序时，才需要传递 `reverse` 参数
gl_num_list.sort(reverse=True)
print(gl_num_list)


"""在参数后使用赋值语句,可以指定参数的缺省值"""
# 必须保证带有默认值的缺省参数在参数列表末尾
def print_info(name, gender=True):
    
    gender_text = "男生"
    if not gender:
        gender_text = "女生"

    print("%s 是 %s" % (name, gender_text))


"""在调用函数时,如果有多个缺省参数,需要指定参数名,这样解释器才能够知道参数的对应关系！"""
def print_info(name, title="", gender=True):
    """

    :param title: 职位
    :param name: 班上同学的姓名
    :param gender: True 男生 False 女生
    """

    gender_text = "男生"

    if not gender:
        gender_text = "女生"

    print("%s%s 是 %s" % (title, name, gender_text))


# 提示：在指定缺省参数的默认值时，应该使用最常见的值作为默认值！
print_info("小明")
print_info("老王", title="班长")  # 在调用函数时,如果有多个缺省参数,需要指定参数名,这样解释器才能够知道参数的对应关系！
print_info("小美", gender=False)
