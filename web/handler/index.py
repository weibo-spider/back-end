import pprint

import tornado.web

import config


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
