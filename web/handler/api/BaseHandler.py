import tornado.web

class BaseHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        # print "setting headers!!!"
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    # def post(self):
    #     self.write('some post')
    #
    # def get(self):
    #     self.write('some get')

    def options(self):
        # no body
        self.set_status(204)
        self.finish()

    def check_parameter(self, list_arguments):
        for v in list_arguments:
            if v not in self.request.arguments:
                return False
        return True
