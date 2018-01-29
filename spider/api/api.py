# -*- coding: UTF-8 -*-
# author:昌维[867597730@qq.com]
# github:https://github.com/cw1997

from spider.api.config import str_user_info_api, str_followers_api, str_fans_api


def generate_user_info_url(int_uid):
    return str_user_info_api % (int_uid, int_uid, int_uid)


def generate_followers_url(int_uid, int_page):
    return str_followers_api % (int_uid, int_page)


def generate_fans_url(int_uid, int_page):
    return str_fans_api % (int_uid, int_page)
