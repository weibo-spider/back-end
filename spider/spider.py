import threading
from pprint import pprint

from common.mongodb.mongodb import insert_many
from spider.fetch.fans.spider import spider_fans
from spider.fetch.followers.spider import spider_followers


class Spider(threading.Thread):
    def __init__(self, task_queue, dict_collections):
        threading.Thread.__init__(self)
        self.task_queue = task_queue
        self.dict_collections = dict_collections
        # for i in range(5):
        #     q.put(i)

    def run(self):
        q = self.task_queue
        # while not q.empty():
        while True:
            task = q.get()
            pprint(task)

            int_uid = task['uid']
            int_page_limit = task['page_limit']
            int_depth_limit = task['depth_limit']

            list_users, list_relations = spider_followers(int_uid, int_page_limit, int_depth_limit)
            insert_many(self.dict_collections['users'], list_users)
            insert_many(self.dict_collections['relations'], list_relations)

            list_users, list_relations = spider_fans(int_uid, int_page_limit, int_depth_limit)
            insert_many(self.dict_collections['users'], list_users)
            insert_many(self.dict_collections['relations'], list_relations)

            q.task_done(task)

def run(spider_thread_num, task_queue, dict_collections):
    # list_thread = []
    for i in range(spider_thread_num):
        thread = Spider(task_queue, dict_collections)
        thread.start()

        # for i in range(spider_thread_num):
        #     list_thread[i].join()
