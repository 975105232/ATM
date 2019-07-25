from conf import settings
import json
import os


# 保存数据
def save(user_dic):
    user_path = f'{settings.DB_PATH}/{user_dic["name"]}.json'

    with open(user_path, 'w', encoding='utf-8') as f:
        json.dump(user_dic, f, ensure_ascii= False)
        f.flush()


# 查找数据
def select(name):
    user_path = f'{settings.DB_PATH}/{name}.json'

    if os.path.exists(user_path):
        with open(user_path, 'r', encoding='utf-8') as f:
            user_dic = json.load(f)
            return user_dic