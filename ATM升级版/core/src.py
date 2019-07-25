from interface import user,bank,shop,admin
from lib import common

user_info = {
    'name': None,
    'is_admin': False
}

# 注册
def register():
    print("注册..")
    while True:
        name = input("请输入用户名：").strip()
        flag = user.check_name_interface(name)
        if flag:
            print("用户已存在！")
            continue
        pwd = input("请输入密码;").strip()
        re_pwd = input("请再次输入密码：").strip()
        if re_pwd == pwd:
            msg = user.register_interface(name, pwd)
            if msg:
                print(msg)
                break
            else:
                print("注册失败！")
        else:
            print("两次输入的密码不一致！")


# 登录
def login():
    print("登录..")
    while True:
        name = input("请输入用户名：").strip()
        flag = user.check_name_interface(name)
        if not flag:
            print("用户不存在！")
            continue
        if name == 'ylj':
            user_info['is_admin'] = True
        else:
            user_info['is_admin'] = False
        pwd = input("请输入密码：").strip()
        flag, msg = user.login_interface(name, pwd)
        if flag:
            print(msg)
            user_info['name'] = name
            break
        else:
            print(msg)

# 查看用户余额
@common.login_auth
def check_balance():
    print("查看余额...")
    bal = user.check_balance_interface(user_info['name'])
    print(bal)

# 提现
@common.login_auth
def withdraw():
    print("提现...")
    while True:
        money = input("请输入提现金额：").strip()
        if not money.isdigit():
            print("请输入正确的数字!")
            continue
        money = int(money)
        flag, msg = bank.withdraw_interface(user_info['name'], money)
        if flag:
            print(msg)
            break
        else:
            print(msg)

# 还款
@common.login_auth
def repay():
    print("还款功能..")
    while True:
        money = input("请输入还款金额：").strip()
        if not money:
            print("请输入正确的数字！")
            continue
        money = int(money)
        msg = bank.repay_interface(user_info['name'], money)

        print(msg)
        break

# 转账
@common.login_auth
def transfer():
    print("转账...")
    while True:
        to_name = input("请输入需要转账的用户：").strip()
        flag = user.check_name_interface(to_name)
        if not flag:
            print("用户不存在！")
            continue

        money = input("请输入需要转账的金额：").strip()
        if not money.isdigit():
            print("请输入正确的数字！")
            continue
        money = int(money)
        flag, msg = bank.transfer_interface(to_name, user_info['name'], money)
        if flag:
            print(msg)
            break
        else:
            print(msg)

# 查看流水
@common.login_auth
def check_flow():
    print("查看流水...")
    flow_list = bank.check_flow_interface(user_info['name'])
    for flow in flow_list:
        print(flow)

# 购物
@common.login_auth
def shopping():
    print("购物...")

    good_list = [
        ['全家桶', 80],
        ['汉堡套餐', 45],
        ['可乐鸡翅', 15],
        ['绝味鸭脖', 20],
        ['烤猪蹄', 10],
    ]

    shop_cart = {}

    cost = 0

    bal = user.check_balance_interface(user_info['name'])

    while True:
        for index, good in enumerate(good_list):
            print(index, good)
        choice = input("请输入商品编号或者q退出:").strip()
        if choice.isdigit():
            choice = int(choice)
            if choice >= 0 and choice < len(good_list):
                good_name,good_price = good_list[choice]
                if bal >= good_price:
                    if good_name in shop_cart:
                        shop_cart[good_name] += 1
                    else:
                        shop_cart[good_name] = 1
                    cost += good_price
                else:
                    print("穷逼，快去充值！")
            else:
                print("请输入正确的商品编号")

        elif choice == 'q':
            commit = input("是否确认购买，请选择y/n:").strip()
            if commit == 'y':
                flag, msg = shop.shop_interface(user_info['name'], cost)
                if flag:
                    print(msg)
                    break
                else:
                    print(msg)
            elif commit == 'n':
                shop.add_shop_cart_interface(user_info['name'], shop_cart)
                break
        else:
            print("请输入正确的数字！")

# 查看购物车
@common.login_auth
def check_shop_cart():
    shop_cart = shop.check_shop_cart_interface(user_info['name'])
    if not shop_cart:
        print("购物车为空，请先购物！")
    print(shop_cart)

# 注销用户
@common.login_auth
def logout():
    print("注销用户..")
    flag, msg = user.logout_interface()
    if flag:
        print(msg)

# 管理员操作
@common.login_auth
def admin_do():
    from core import admin_src
    if user_info['is_admin'] == True:
        return admin_src.admin_do()
    else:
        return '抱歉，您不是管理员'

func_dic = {
    '1': register,
    '2': login,
    '3': check_balance,
    '4': withdraw,
    '5': repay,
    '6': transfer,
    '7': check_flow,
    '8': shopping,
    '9': check_shop_cart,
    '10': logout,
    '11': admin_do,
}

def run():
    while True:
        print('''
        1.注册
        2.登录
        3.查看用户余额
        4.提现
        5.还款
        6.转账
        7.查看流水
        8.购物
        9.查看购物车
        10.注销用户
        11.管理员
        q.退出程序
        ''')
        choice = input("请选择功能编号：").strip()

        if choice == 'q':
            break
        elif choice in func_dic:
            func_dic[choice]()
        else:
            print("请输入正确的编号！")