import tornado.wsgi
import wsgiref.handlers
import os.path
import sys

sys.path.append(os.path.dirname(__file__))
import config

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
)

application = tornado.wsgi.WSGIApplication(config.handlerlist, **settings)
wsgiref.handlers.CGIHandler().run(application)