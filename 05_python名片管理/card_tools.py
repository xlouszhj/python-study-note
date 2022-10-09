# 定义空列表 记录所有的名片字典
card_list = []


# 显示菜单
def show_menu():
    """显示菜单"""

    print("*" * 50)
    print("欢迎使用【名片管理系统】 V1.0")
    print()
    print("1. 新增名片")
    print("2. 显示名片")
    print("3. 搜索名片")
    print()
    print("0. 退出系统")
    print("*" * 50)


# 新增名片
def new_card():
    """新增名片"""

    print("-" * 50)
    
    # 提示用户输入名片的详细信息
    name_str = input("请输入姓名: ")
    phone_str = input("请输入电话: ")
    qq_str = input("请输入QQ: ")
    email_str = input("请输入邮箱: ")

    # 使用用户输入的信息建立名片字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "QQ": qq_str,
                 "email": email_str}
    
    # 将名片字典添加到列表中
    card_list.append(card_dict)

    # 提示用户名片添加成功
    print("添加 %s 的名片成功！" % name_str)


# 显示名片
def show_cards():
    """显示名片"""

    print("-" * 50)
    print("功能: 显示所有名片")

    # 判断是否存在名片记录,如果没有,提示用户并且返回
    if len(card_list) == 0:
        print("当前没有任何名片记录, 请使用新增功能添加名片！")
        
        # return 可以返回一个函数的执行结果
        # 下方的代码不会被执行
        # 如果 return 后面没有任何内容, 表示会返回到调用函数的位置
        # 并且不会返回任何的结果
        return 

    # 如果有名片记录 显示名片信息
    # 打印表头
    for head in ["姓名","电话","QQ","邮箱"]:
        print(head,end="\t\t")  # 加上水平制表符 显示的更整齐
    
    print()  # 换行
    
    #打印分割线
    print("=" * 50)

    for card_dict in card_list:  # 在列表中遍历的是字典
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["QQ"],
                                        card_dict["email"]))


# 搜索名片
def search_card():
    """搜索名片"""

    print("-" * 50)
    print("功能: 搜索名片")

    # 提示用户输入要搜索的姓名
    find_name = input("请输入要搜索的姓名: ")

    for card_dict in card_list:
        if card_dict["name"] == find_name:
            
            # 打印表头
            for head in ["姓名","电话","QQ","邮箱"]:
                print(head,end="\t\t")  # 加上水平制表符 显示的更整齐
        
            print()  # 换行
        
            #打印分割线
            print("=" * 50)

            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["QQ"],
                                            card_dict["email"]))
        
            # 针对找到的名片记录执行修改和删除的操作
            # 定义一个 deal_card 函数来执行修改和删除操作
            deal_card(card_dict)

            break
    
    else:
        print("抱歉, 没有找到 %s 的名片记录" % find_name)


# 定义一个 deal_card 函数来执行名片的修改和删除操作
def deal_card(find_dict):
    
    """名片处理函数
       find_dict: 查找到的名片字典 """

    action_str = input("请输入要执行的操作:\n"
                       " [1]修改 [2]删除 [0]返回上一级菜单: ")

    if action_str == "1":
        # 修改名片
        # 系统中的 input 函数无法做到回车不修改信息,所以可以自己定义一个 input_card_info 函数来实现
        find_dict["name"] = input_card_info(find_dict["name"], "修改姓名为[回车不修改]:")
        find_dict["phone"] = input_card_info(find_dict["phone"], "修改电话为[回车不修改]:")
        find_dict["QQ"] = input_card_info(find_dict["QQ"], "修改QQ为[回车不修改]:")
        find_dict["email"] = input_card_info(find_dict["email"], "修改邮箱为[回车不修改]:")
        
        print("修改名片成功！")

    elif action_str == "2":
        # 删除名片
        card_list.remove(find_dict)
        print("删除名片成功!")

    elif action_str == "0":
        # 返回上一级菜单
        return 


# 定义一个 input_card_info 函数来实现回车不修改内容
def input_card_info(dict_value,tip_message):
    """dict_value: 字典原有的值  tip_message: 输入的提示文字"""

    # 用户输入内容
    result_str = input(tip_message)

    # 针对用户输入的内容进行判断,如果用户输入了内容,直接返回结果
    if len(result_str) > 0:
        return result_str
    # 如果用户没有输入内容,返回字典中原有的值
    else:
        return dict_value