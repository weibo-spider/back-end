# -*- coding: UTF-8 -*-
# author:昌维[867597730 @ qq.com]
# github:https://github.com/cw1997
import pprint

import pymongo
import tornado.web

import config
from common.task.task import TaskQueue

# C:\Users\Administrator>ab -n 10000 -c 100 http://127.0.0.1:8888/add_task?uid=11&
# user_name=1
from spider.fetch.user.spider import get_name_by_uid, get_uid_by_name
from web.handler.api.BaseHandler import BaseHandler
from web.handler.error import Error
from web.handler.render import json_return
from web.helper.database import select, select_by_page


class ListTaskHandler(BaseHandler):
    def get(self):
        str_page_size_key = 'page_size'
        str_page_key = 'page'
        str_last_key = 'last'
        str_ret = ''
        if not self.check_parameter((str_page_size_key, str_page_key, str_last_key)):
            str_ret = json_return(Error.ERROR_GET_TASK_PAGE_PARAM_ERROR)
        else:
            int_page_size, int_page, int_last = int(self.get_argument(str_page_size_key)), int(self.get_argument(str_page_key)), int(self.get_argument(str_last_key))
            list_task, int_count, int_last_time = select_by_page(config.mongodb_task_queue_collection, {}, 'create_time', pymongo.DESCENDING, int_page_size, int_page, int_last)
            str_ret = json_return(Error.ERROR_OK, {'tasks': list_task, 'count': int_count, 'last': int_last_time})
        self.write(str_ret)


class AddTaskHandler(BaseHandler):
    """
    http://127.0.0.1:8888/add_task?uid=1934383474&page_limit=1&depth_limit=1
    """
    def get(self):
        int_uid = 0
        str_name = ''
        ret = ''
        task = {}
        if not self.check_parameter(('page_limit', 'depth_limit', 'uid', 'username')):
            print('parameter error')
            ret = json_return(Error.ERROR_GET_TASK_ADD)
            self.write(ret)
            return
        if 'uid' in self.request.arguments:
            int_uid = int(self.get_argument('uid'))
            str_name = get_name_by_uid(int_uid)

        elif 'username' in self.request.arguments:
            str_name = self.get_argument('username')
            int_uid = get_uid_by_name(str_name)
        else:
            ret = json_return(Error.ERROR_GET_TASK_ADD)
            self.write(ret)

        if str_name == '' or int_uid == 0:
            ret = json_return(Error.ERROR_GET_TASK_ADD_FREQUENTLY)
            self.write(ret)
            return

        task = {
            'uid': int_uid,
            'name': str_name,
            'ip': self.request.remote_ip,
            'page_limit': int(self.get_argument('page_limit')),
            'depth_limit': int(self.get_argument('depth_limit')),
        }
        int_task_add = str(TaskQueue.put(task))
        # pprint.pprint(int_task_add)
        if int_task_add:
            ret = json_return(Error.ERROR_OK, int_task_add)
        else:
            ret = json_return(Error.ERROR_GET_TASK_ADD, task)
        self.write(ret)

        def post(self):
            self.get(self)
