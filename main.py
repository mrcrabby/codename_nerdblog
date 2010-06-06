import tornado.httpserver
import tornado.options
import tornado.ioloop
import tornado.web
import os.path
import config

dev_settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    debug = True
)

for spath in ('css','images','js'):
    static_path = os.path.join(os.path.dirname(__file__), "static/%s" % spath)
    config.handlerlist.append((r"/%s/(.*)" % spath, tornado.web.StaticFileHandler,dict(path = static_path)))

application = tornado.web.Application(config.handlerlist, **dev_settings)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()