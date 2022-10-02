print("Hello World")
# 加\n可换行 
print("你好 世界\n\n你好 python") 
"""
在默认情况下, print 函数输出内容之后,会自动在内容末尾增加换行
如果不希望末尾增加换行,可以在 print 函数输出内容的后面增加 end=""
其中 "" 中间可以指定 print 函数输出内容之后,继续希望显示的内容
"""
# 单纯的换行
print("")
# 向控制台输出内容结束之后，不会换行
print("hello python", end="")
print("你看看换行了吗？")