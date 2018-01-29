# -*- coding: UTF-8 -*-
# author:昌维[867597730 @ qq.com]
# github:https://github.com/cw1997

import pprint

import requests


def fetch(url):
    r = requests.get(url)
    str_ret = r.text
    # TODO:debug info
    print(url)
    return str_ret


if __name__ == '__main__':
    pprint.pprint(fetch('https://www.baidu.com'))
