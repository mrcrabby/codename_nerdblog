import tornado.wsgi
import wsgiref.handlers
import sys
sys.path.append('/var/www')
import config

application = tornado.wsgi.WSGIApplication(config.handlerlist)
wsgiref.handlers.CGIHandler().run(application)