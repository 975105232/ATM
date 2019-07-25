from db import db_handler
from interface import bank
from lib import common

shop_logger = common.get_logger('shop')
# 购物接口
def shop_interface(name, cost):
    flag = bank.pay_interface(name, cost)
    if flag:
        msg1 = f'用户{name}购买成功！'
        shop_logger.info(msg1)
        return True, msg1
    msg2 = f'用户{name}购买失败！'
    shop_logger.info(msg2)
    return False, msg2

# 添加购物车接口
def add_shop_cart_interface(name, shop_cart):
    user_dic = db_handler.select(name)

    old_cart = user_dic['shop_cart']

    for shop in shop_cart:
        if shop in old_cart:
            num = shop_cart[shop]

            old_cart[shop] += num
        else:
            num = shop_cart[shop]

            old_cart[shop] = num
    user_dic['shop_cart'].update(old_cart)
    db_handler.save(user_dic)
    msg = f'用户{name}添加商品成功！'
    shop_logger.info(msg)
    return True, msg

# 查看购物车
def check_shop_cart_interface(name):
    user_dic = db_handler.select(name)
    shop_logger.info(f"用户{name}查看了购物车")
    return user_dic['shop_cart']

