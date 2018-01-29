# -*- coding: UTF-8 -*-
# author:昌维[867597730@qq.com]
# github:https://github.com/cw1997

from spider.fetch.fans.helper import get_fans_json, get_fans_by_json, get_relation


def spider_fans_pages(int_uid, int_page_limit):
    list_users = []
    list_relations = []
    # for v in range(int_page_limit * 20):
    #     list_users.append(v)
    #     list_relations.append(v)
    for int_page in range(1, int_page_limit + 1):
        dict_fans_json = get_fans_json(int_uid, int_page)
        list_users += get_fans_by_json(dict_fans_json)
        list_relations += get_relation(int_uid, list_users)
    return list_users, list_relations


def spider_fans_users(list_users, int_page_limit):
    list_users_result = []
    list_relations_result = []
    for user in list_users:
        list_users_return, list_relations_return = spider_fans_pages(user.get('id'), int_page_limit)
        # list_users_return, list_relations_return = spider_fans_pages(1, int_page_limit)
        list_users_result += list_users_return
        list_relations_result += list_relations_return
    return list_users_result, list_relations_result


def spider_fans_depths(list_users, int_page_limit, int_depth):
    """
    递归遍历fans列表，先进入最深处开始遍历，然后逐层回归到第一层
    :param list_users:
    :param int_page_limit:
    :param int_depth:
    :return:
    """
    # 如果递归深度仍然大于0，那么继续往更深处递归
    if int_depth > 0:
        # 获取当前一级深度的用户信息以及关系信息
        list_users_current_depth, list_relations_current_depth = spider_fans_users(list_users, int_page_limit)
        # 获取下一级深度的用户信息以及关系信息
        list_users_next_depth, list_relations_next_depth = spider_fans_depths(list_users_current_depth, int_page_limit, int_depth-1)
        # 汇总下一级深度的信息以及当前深度的信息返回
        list_users_return = list_users_next_depth + list_users_current_depth
        list_relations_return = list_relations_next_depth + list_users_current_depth
        return list_users_return, list_relations_return
    else:
        return [], []


def spider_fans(int_uid, int_page_limit, int_depth):
    list_my_fans_result, list_my_relations_result = spider_fans_pages(int_uid, int_page_limit)
    # 因为上一行代码遍历"我的粉丝"已经算一级深度了，所以自减1
    int_depth -= 1
    list_users_return, list_relations_return = spider_fans_depths(list_my_fans_result, int_page_limit, int_depth)
    # 汇总信息并且返回
    list_users = list_my_fans_result + list_users_return
    list_relations = list_my_relations_result + list_relations_return
    return list_users, list_relations
