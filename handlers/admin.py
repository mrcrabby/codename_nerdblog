from tornado.web import RequestHandler as ReqHandler


class RootHandler(ReqHandler):
    def get(self):
        self.render("admin/root.html", extrajs = ["admin.js"])
        
class AjaxCreateFormHandler(ReqHandler):
    def get(self):
        self.write({"html": self.render_string("admin/createarticle.html")})