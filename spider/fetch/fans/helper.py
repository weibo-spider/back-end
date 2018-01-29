# -*- coding: UTF-8 -*-
# author:昌维[867597730@qq.com]
# github:https://github.com/cw1997

from spider.api.api import generate_fans_url
from spider.util.request import fetch
from spider.util.json import json_decode


def get_fans_json(int_uid, int_page):
    url = generate_fans_url(int_uid, int_page)
    str_fans_json = fetch(url)
    try:
        dict_fans_json = json_decode(str_fans_json)
    except:
        print('get_fans_json error:[%s]%s' % (url, str_fans_json))
        return {}
    return dict_fans_json


def get_fans_by_json(dict_fans_json):
    """
    # user's field:
    # id
    # screen_name
    # gender
    # description
    # avatar_hd
    # statuses_count
    # followers_count
    # follow_count
    # verified
    :param dict_fans_json:dict
    :return:list
    """
    bol_ok = dict_fans_json.get('ok', 0)
    if not bol_ok:
        return []
    else:
        list_users = []
        list_users_raw = dict_fans_json['data']['cards'][0]['card_group']
        for v in list_users_raw:
            user = v.get('user', None)
            if user is not None:
                list_users.append(user)
        return list_users


def get_relation(int_my_uid, list_users):
    list_relations = []
    for v in list_users:
        list_relations.append({'source':v.get('id'), 'target':int_my_uid})
    return list_relations
