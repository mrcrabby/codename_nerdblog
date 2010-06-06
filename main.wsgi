import tornado.wsgi
import wsgiref.handlers
import sys
sys.path.append('/var/www')
import config

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
)

application = tornado.wsgi.WSGIApplication(config.handlerlist, **settings)
wsgiref.handlers.CGIHandler().run(application)