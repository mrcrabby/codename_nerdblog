import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World... This Means it is working?")