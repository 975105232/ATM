from lib import common
from db import db_handler

bank_logger = common.get_logger('bank')


# 提现接口
def withdraw_interface(name, money):
    user_dic = db_handler.select(name)
    if user_dic['balance'] >= money * 1.05:
        user_dic['balance'] -= money * 1.05
        msg = f'用户{name}提现{money}元成功！'

        user_dic['flow'].append(msg)
        bank_logger.info(msg)
        db_handler.save(user_dic)
        return True, msg
    else:
        return False, '穷逼，快去充钱！'

# 还款接口
def repay_interface(name, money):
    user_dic = db_handler.select(name)
    user_dic['balance'] += money
    msg = f'用户{name}还款{money}元成功！'
    bank_logger.info(msg)
    user_dic['flow'].append(msg)
    db_handler.save(user_dic)
    return msg

# 转账接口
def transfer_interface(to_name, from_name, money):
    to_user_dic = db_handler.select(to_name)
    from_user_dic = db_handler.select(from_name)

    if from_user_dic['balance'] >= money:
        from_user_dic['balance'] -= money
        to_user_dic['balance'] += money

        from_user_flow = f'用户{from_name}转账{money}元给了用户{to_name}'
        to_user_flow = f'用户{to_name}接收到了用户{from_name}的转账{money}元'

        bank_logger.info(from_user_flow)
        bank_logger.info(to_user_flow)

        from_user_dic['flow'].append(from_user_flow)
        to_user_dic['flow'].append(to_user_flow)
        db_handler.save(from_user_dic)
        db_handler.save(to_user_dic)
        return True, from_user_flow
    return False, '穷逼。快去充钱！'

# 查看流水接口
def check_flow_interface(name):
    user_dic = db_handler.select(name)
    bank_logger.info(f'用户{name}查看的了流水')
    return user_dic['flow']

# 银行支付接口
def pay_interface(name, cost):
    user_dic = db_handler.select(name)
    if user_dic['balance'] >= cost:
        user_dic['balance'] -= cost
        db_handler.save(user_dic)

        msg = f'用户{name}支付成功{cost}元'
        user_dic['flow'].append(msg)
        bank_logger.info(msg)
        return True, msg
    return False, '余额不足，请充值！'


