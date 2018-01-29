import pymongo

import config
from common.mongodb.mongodb import conn_mongodb, select_database, select_collection


def get_collection(str_collection_name):
    mongodb = conn_mongodb(config.mongodb_host, config.mongodb_port)
    db = select_database(mongodb, config.mongodb_database)
    return select_collection(db, str_collection_name)

def select(str_collection_name, dict_where):
    collection = get_collection(str_collection_name)
    cursor = collection.find(dict_where)
    list_record = list(cursor)
    return _delete_id(list_record)

def select_by_page(str_collection_name, dict_where, str_order_key, order_type, int_page_size, int_page, int_last):
    collection = get_collection(str_collection_name)
    dict_where[str_order_key] = {"$gt": int_last}
    cursor = collection.find(dict_where).sort(str_order_key, order_type)
    int_count = cursor.count()
    if int_count < 1:
        return [], int_count, -1
    cursor_sort = cursor.sort(str_order_key, order_type)
    cursor_page = cursor_sort.skip((int_page-1)*int_page_size).limit(int_page_size)
    print(cursor_page.count())
    list_record = list(cursor_page)
    int_last_time = list_record[len(list_record)-1][str_order_key] - 1
    return _delete_id(list_record), int_count, int_last_time

def _delete_id(list_record):
    for v in list_record:
        del v['_id']
    return list_record
