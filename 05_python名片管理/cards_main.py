import card_tools
while True:
    
    # 显示系统菜单
    card_tools.show_menu()

    # 用户进行操作
    action = input("请选择操作功能：")
    print("您选择的操作是：%s" % action)

    # 根据用户输入决定后续的操作
    if action in ["1", "2", "3"]:
        
        # 新增名片
        if action == "1":
            card_tools.new_card()
        
        # 显示名片
        elif action == "2":
            card_tools.show_cards()
        
        # 搜索名片
        elif action == "3":
            card_tools.search_card()
    
    # 用户选择退出系统
    elif action == "0":
        
        print("欢迎再次使用【名片管理系统】")
        break

    else:
        print("输入错误，请重新输入")
