import tornado.ioloop
import tornado.web

from web.handler.api.v1 import task
from web.handler.index import MainHandler


def run(port=80):
    str_api_v1 = '/api/v1/'
    application = tornado.web.Application([
        ("/", MainHandler),
        (str_api_v1 + "task/add", task.AddTaskHandler),
        (str_api_v1 + "task/list", task.ListTaskHandler),
    ])
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()
