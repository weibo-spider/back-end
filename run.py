import pprint
import queue

import config
from common.mongodb.mongodb import conn_mongodb, select_database, select_collection, insert_many
from common.task.task import TaskQueue
from spider import spider
from web import web

mongodb = conn_mongodb(config.mongodb_host, config.mongodb_port)
db = select_database(mongodb, config.mongodb_database)
users_collection = select_collection(db, config.mongodb_users_collection)
relations_collection = select_collection(db, config.mongodb_relations_collection)
task_queue_collection = select_collection(db, config.mongodb_task_queue_collection)

TaskQueue.init(task_queue_collection)

dict_collections = {
    'users': users_collection,
    'relations': relations_collection,
    'task_queue': task_queue_collection,
}

spider.run(config.spider_thread_num, TaskQueue, dict_collections)

web.run(config.web_server_port)
