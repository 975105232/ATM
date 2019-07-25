from interface import user,admin



# 冻结
def lock():
    print("冻结用户...")
    name = input("请输入需要冻结的用户:").strip()
    flag = user.check_name_interface(name)
    if flag:
        msg = admin.lock_interface(name)
        print(msg)
    else:
        print("用户不存在！")

# 解冻
def unlock():
    print("解冻..")
    name = input("请输入需要解冻的用户:").strip()
    flag = user.check_name_interface(name)
    if flag:
        msg = admin.unlock_interface(name)
        print(msg)
    else:
        print("用户不存在！")

# 修改用户额度
def change_bal():
    print("修改用户额度..")
    name = input("请输入需要修改额度的用户：").strip()
    flag = user.check_name_interface(name)
    if not flag:
        print("用户不存在！")
        return
    limit = input("请输入需要修改额度：").strip()
    if limit.isdigit():
        limit = int(limit)

        msg = admin.change_balance_interface(name, limit)
        print(msg)
    else:
        print("请输入数字！")

admin_dic = {
    '1': lock,
    '2': unlock,
    '3': change_bal,
}

def admin_do():
    while True:
        print('''
        1.冻结用户
        2.解冻用户
        3.修改用户额度
        q.退出程序
        ''')
        choice = input("请选择功能编号：").strip()

        if choice == 'q':
            break
        elif choice in admin_dic:
            admin_dic[choice]()
        else:
            print("请输入正确的编号！")