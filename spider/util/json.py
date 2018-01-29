# -*- coding: UTF-8 -*-
# author:昌维[867597730 @ qq.com]
# github:https://github.com/cw1997

import pprint
import json


def json_decode(str_json):
    return json.loads(str_json)


def json_encode(dict_json):
    return json.dumps(dict_json)


def json_dump(str_json):
    pprint.pprint(json_decode(str_json))
