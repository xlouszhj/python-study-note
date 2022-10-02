"""
字符串 就是一串字符，是编程语言中表示文本的数据类型
在 Python 中可以使用 一对双引号 `"` 或者 一对单引号 `'` 定义一个字符串
  虽然可以使用 `\"` 或者 `\'` 做字符串的转义,但是在实际开发中:
    如果字符串内部需要使用 `"`，可以使用 `'` 定义字符串
    如果字符串内部需要使用 `'`，可以使用 `"` 定义字符串
可以使用 索引[] 获取一个字符串中 指定位置的字符,索引计数从 0 开始
也可以使用 `for` 循环遍历 字符串中每一个字符
"""
str1 = "Hello Python"
str2 = '我的外号是"大西瓜"'
str3 = "我的外号是'大西瓜'"

for char in str1:
    print(char,end="")
print()

print(str2)
print(str3)

# 统计字符串长度
print(len(str1))

# 统计某一个子字符串出现的次数
print(str1.count("llo"))
print(str1.count("abc"))  # 不会报错 会输出0次

# 某一个子字符串出现的位置
print(str1.index("llo"))
# print(str1.index("abc"))  报错 
