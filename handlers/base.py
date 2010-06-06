import tornado.web
from servers import redisDB

class BaseHandler(tornado.web.RequestHandler):
    def get(self):
        if redisDB.exists("foo"):
            redisDB.incr("foo")
        else:
            redisDB["foo"] = 0
        
        self.render("base.html",foo = redisDB["foo"])