name_list = ["张三","李四","王五","王小二"]

"""
顺序的从列表中依次获得数据,每一次循环过程中,数据都会保存在my_name(自己定义的)这个变量中，
在循环体内部可以访问到当前这一次获取到的数据

for 循环体内部使用的变量名 in 列表变量名:
    print("我的名字是： %s " % my_name)

"""

for my_name in name_list:
    print("我的名字是： %s " % my_name)
