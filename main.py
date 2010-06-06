import tornado.httpserver
import tornado.options
import tornado.ioloop
import tornado.web
import config

application = tornado.web.Application(config.handlerlist, debug = True)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()