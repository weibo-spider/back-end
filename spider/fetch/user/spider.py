# -*- coding: UTF-8 -*-
# author:昌维[867597730@qq.com]
# github:https://github.com/cw1997
import pprint

from spider.fetch.user.helper import get_user_json, get_user_info_by_json


def get_user_info(int_uid):
    dict_json = get_user_json(int_uid)
    pprint.pprint(dict_json)
    return get_user_info_by_json(dict_json)

def get_name_by_uid(int_uid):
    dict_user = get_user_info(int_uid)
    str_name = dict_user.get('screen_name', '')
    return str_name

def get_uid_by_name(str_name):
    return ''
