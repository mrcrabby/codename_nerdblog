import tornado.httpserver
import tornado.options
import tornado.ioloop
import tornado.web
import os.path
import config

dev_settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    debug = True
)

application = tornado.web.Application(config.handlerlist, **dev_settings)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()