# -*- coding: UTF-8 -*-
# author:昌维[867597730 @ qq.com]
# github:https://github.com/cw1997


# 爬虫线程数量
spider_thread_num = 10
# web服务器端口
web_server_port = 8888

# MongoDB数据库IP
mongodb_host = '127.0.0.1'
# MongoDB数据库端口
mongodb_port = 27017
# MongoDB数据库名字
mongodb_database = 'weibo-spider'

# ---------- 以下内容不建议修改 ----------

# 微博用户信息集合
mongodb_users_collection = 'users'
# 微博用户关注关系集合
mongodb_relations_collection = 'relations'
# 抓取人物队列集合
mongodb_task_queue_collection = 'task'
# 日志集合
mongodb_log_collection = 'log'
