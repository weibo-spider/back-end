import pprint

from common.mongodb.mongodb import conn_mongodb, select_database, select_collection, insert_many
from spider.api.config import int_test_uid
from spider.fetch.fans.spider import spider_fans
from spider.fetch.followers.spider import spider_followers
from spider.fetch.user.spider import get_user_info



pprint.pprint(get_user_info(int_test_uid))

exit()

int_page_limit = 1
int_depth = 1

# task_num ~= p * 20 + (p * 20) ^ d
# list_users len:894, list_relations len:954
# list_users len:80, list_relations len:140
# int_page_limit = 3 int_depth = 3 list_users len:180, list_relations len:240
# int_page_limit = 2 int_depth = 3 list_users len:120, list_relations len:140
# int_page_limit = 1 int_depth = 3 list_users len:1210, list_relations len:1210
print('spider_fans task num: %d' % ((int_page_limit) * 20 + pow((int_page_limit * 20), int_depth)))

list_users, list_relations = spider_followers(int_test_uid, int_page_limit, int_depth)

print(list_users)
print(list_relations)
# pprint.pprint(list_users)
# pprint.pprint(list_relations)
print('list_users len:%d, list_relations len:%d' % (len(list_users), len(list_relations)))


mongodb = conn_mongodb()
db = select_database(mongodb, 'weibo')
collection = select_collection(db, 'users')
pprint.pprint(insert_many(collection, list_users))
collection = select_collection(db, 'relations')
pprint.pprint(insert_many(collection, list_relations))


