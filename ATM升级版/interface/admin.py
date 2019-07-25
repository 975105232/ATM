from db import db_handler
from lib import common

admin_logger = common.get_logger('admin')

# 冻结用户接口
def lock_interface(name):
    user_dic = db_handler.select(name)

    user_dic['lock'] = True
    msg = f'用户{name}已冻结！'
    admin_logger.info(msg)
    db_handler.save(user_dic)

    return msg

# 解冻用户接口
def unlock_interface(name):
    user_dic = db_handler.select(name)

    user_dic['lock'] = False
    msg = f'用户{name}已解冻！'
    admin_logger.info(msg)
    db_handler.save(user_dic)

    return msg

# 修改用户额度接口
def change_balance_interface(name, limit):
    user_dic = db_handler.select(name)
    user_dic['balance'] = limit
    msg = f'用户{name}额度修改为{limit}元'
    db_handler.save(user_dic)
    admin_logger.info(msg)

    return msg

