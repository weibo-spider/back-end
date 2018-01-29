from spider.util.json import json_encode
from web.handler.error import Error


def json_return(error, data=''):
    dict_return = dict()
    dict_return['errorno'] = error
    dict_return['errormsg'] = Error.get_description(error)
    dict_return['data'] = data
    return json_encode(dict_return)
