def print_line(char,times):
    """
    打印任意字符重复任意次数的分割线
    char : 分割线字符形式
    times : 分割线字符重复次数
    """

    print(char * times)


def printLines(time1,char,times):
    """
    打印任意行分割线,且分割线符合上述函数的要求
    time1 : 分割线行数
    """

    row = 0
    while row < time1:
        print_line(char,times)
        row += 1

# 打印5行由'-'重复20次组成的分割线
printLines(5,'-',20)
  