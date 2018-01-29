import queue

import time

from common.mongodb.mongodb import sort_result, ORDER_ASC, insert_one, find_many, find_one, update


class TaskQueue(object):
    task_queue = None

    task_status = (
        'undefined',
        'unprocessed',
        'processing',
        'processed',
        'error',
        'deleted',
    )

    @staticmethod
    def init(task_collection):
        # TaskQueue.q = queue.Queue()
        TaskQueue.task_queue = task_collection

    @staticmethod
    def get():
        # bol_ok = False
        list_task = []
        while True:
            list_task = find_many(
                TaskQueue.task_queue,
                {'status': TaskQueue.task_status.index('unprocessed')}
            )
            if list_task.count() < 1:
                time.sleep(10)
            else:
                break

        list_task = sort_result(list_task, 'create_time', ORDER_ASC)
        dict_task_old = list_task[0]
        # print(dict_task_old['status'])
        dict_task_new = dict_task_old
        dict_task_new['status'] = TaskQueue.task_status.index('processing')
        dict_task_new['start_time'] = int(time.time())
        # print(dict_task_old['status'])
        update(TaskQueue.task_queue, dict_task_old, dict_task_new)
        return list_task[0]

    @staticmethod
    def task_done(dict_task_old):
        if not dict_task_old:
            return False
        dict_task_new = find_one(
            TaskQueue.task_queue,dict_task_old
        )
        if not dict_task_new:
            return False
        dict_task_new = dict_task_old
        dict_task_new['status'] = TaskQueue.task_status.index('processed')
        dict_task_new['end_time'] = int(time.time())
        update(TaskQueue.task_queue, dict_task_old, dict_task_new)
        return True

    @staticmethod
    def put(dict_task):
        dict_task['create_time'] = int(time.time())
        dict_task['status'] = TaskQueue.task_status.index('unprocessed')
        return insert_one(TaskQueue.task_queue, dict_task)
