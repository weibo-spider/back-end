# -*- coding: UTF-8 -*-
# author:昌维[867597730@qq.com]
# github:https://github.com/cw1997

from spider.api.api import generate_followers_url
from spider.util.request import fetch
from spider.util.json import json_decode


def get_followers_json(int_uid, int_page):
    url = generate_followers_url(int_uid, int_page)
    str_followers_json = fetch(url)
    # print(str_followers_json)
    try:
        dict_followers_json = json_decode(str_followers_json)
    except:
        print('get_fans_json error:[%s]%s' % (url, str_followers_json))
        return {}
    return dict_followers_json


def get_followers_by_json(dict_followers_json):
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
    :param dict_followers_json:dict
    :return:list
    """
    bol_ok = dict_followers_json.get('ok', 0)
    if not bol_ok:
        return []
    else:
        list_users = []
        list_all_followers = get_all_follower(dict_followers_json['data']['cards'])
        list_users_raw = list_all_followers[0]['card_group']
        for v in list_users_raw:
            user = v.get('user', None)
            if user is not None:
                list_users.append(user)
        return list_users


def get_relation(int_my_uid, list_users):
    """
    获取关注关系，注意source和target的正确性
    :param int_my_uid:
    :param list_users:
    :return:
    """
    list_relations = []
    for v in list_users:
        list_relations.append({'source':int_my_uid, 'target':v.get('id')})
    return list_relations


def get_all_follower(cards):
    """
    因为实际获取到的cards字段里面还有别的无关信息，此处过滤出来
    :param cards:
    :return:
    """
    return [i for i in cards if i.get('title') == "他的全部关注" or i.get('title') == "她的全部关注"]
    # all_follower = filter(lambda i: i.get('title') == "他的全部关注" or i.get('title') == "她的全部关注", cards)
