# -*- coding: UTF-8 -*-
# author:昌维[867597730@qq.com]
# github:https://github.com/cw1997
import pymongo
from pymongo import MongoClient


ORDER_ASC = pymongo.ASCENDING
ORDER_DESC = pymongo.DESCENDING


def conn_mongodb(host='localhost', port=27017):
    client = MongoClient(host, port)
    return client


def select_database(client, str_database_name):
    db = client[str_database_name]
    return db


def select_collection(database, str_collection_name):
    collection = database[str_collection_name]
    return collection


def insert_one(collection, dict_data):
    inserted_id = collection.insert_one(dict_data).inserted_id
    return inserted_id


def insert_many(collection, list_data):
    if len(list_data) > 0:
        inserted_ids = collection.insert_many(list_data).inserted_ids
        return inserted_ids
    return -1


def find_one(collection, dict_where):
    result = collection.find_one(dict_where)
    return result


def find_many(collection, dict_where):
    results = collection.find(dict_where)
    return results


def sort_result(result, str_order_key, order_type):
    return result.sort(str_order_key, order_type)

# db.Account.find().sort("UserName",pymongo.ASCENDING)   --升序
# db.Account.find().sort("UserName",pymongo.DESCENDING)  --降序

def update(collection, dict_old, dict_new):
    return collection.update(dict_old, dict_new)

# db = client['test-database']
# collection = db['test-collection']
# posts = db.posts
# post_id = posts.insert_one(post).inserted_id

# class Mongo(object):
#     client = None
#     db = None
#     def __init__(self, host='localhost', port=27017, str_database_name=''):
#         self.client = self._conn(host, port)
#         self.db = self.client[str_database_name]
#
#     def select(self, str_collection, where):
#         self.db[str_collection].find_many(where)
#
#     def _conn(self, host, port):
#         client = MongoClient(host, port)
#         return client
