import hashlib
import logging.config
from conf import settings

# 加密
def get_md5(pwd):
    val = "提莫一米五"
    md5 = hashlib.md5()
    md5.update(pwd.encode('utf-8'))
    md5.update(val.encode('utf-8'))

    res = md5.hexdigest()
    return res

# 用户认证装饰器
def login_auth(func):
    from core import src
    def inner(*args, **kwargs):
        if src.user_info['name']:
            res = func(*args, **kwargs)
            return res
        else:
            print("请先登录！")
            src.login()
    return inner

# 日志功能
def get_logger(type_name):
    logging.config.dictConfig(settings.LOGGING_DIC)
    logger = logging.getLogger(type_name)
    return logger


