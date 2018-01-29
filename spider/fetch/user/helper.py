# -*- coding: UTF-8 -*-
# author:昌维[867597730@qq.com]
# github:https://github.com/cw1997

import pprint

from spider.api.api import generate_user_info_url
from spider.api.config import int_test_uid
from spider.util.json import json_decode
from spider.util.request import fetch


def get_user_json(int_uid):
    url = generate_user_info_url(int_uid)
    str_json = fetch(url)
    # print(str_followers_json)
    dict_json = json_decode(str_json)
    return dict_json


def get_user_info_by_json(dict_json):
    bol_ok = dict_json['ok']
    if not bol_ok:
        return {}
    return dict_json['data']['userInfo']


if __name__ == '__main__':
    pprint.pprint(get_user_json(int_test_uid))
