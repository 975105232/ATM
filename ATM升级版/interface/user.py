from db import db_handler
from lib import common

user_logger = common.get_logger('name')

# 查看用户接口
def check_name_interface(name):
    user_dic = db_handler.select(name)
    if user_dic:
        return True

# 注册接口
def register_interface(name, pwd, balance=15000):
    pwd = common.get_md5(pwd)
    user_dic = {
        'name': name,
        'pwd': pwd,
        'balance': balance,
        'flow': [],
        'shop_cart': {},
        'lock': False
    }
    db_handler.save(user_dic)
    msg = f"用户{name}注册成功"
    user_logger.info(msg)

    return msg

# 登录接口
def login_interface(name, pwd):
    user_dic = db_handler.select(name)
    if user_dic['lock']:
        user_logger.info(f'用户[{name}]已被冻结,请联系管理员!')
        return False, '用户已被冻结，请联系管理员'
    pwd = common.get_md5(pwd)
    if pwd == user_dic['pwd']:
        msg1 = f'用户{name}登陆成功！'
        user_logger.info(msg1)
        return True, msg1
    else:
        msg2 = f'用户{name}密码错误，登录失败！'
        user_logger.info(msg2)
        return False, msg2

# 查看余额接口
def check_balance_interface(name):
    user_dic = db_handler.select(name)
    user_logger.info(f'用户{name}查看了余额')
    return user_dic['balance']

# 注销用户
def logout_interface():
    from core import src
    name = src.user_info['name']
    src.user_info['name'] = None
    msg = f'用户{name}已注销'
    user_logger.info(msg)
    return True, msg






