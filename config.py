from handlers import base, admin

handlerlist = [(r'/', base.BaseHandler),
               (r'/admin', admin.RootHandler),
               (r'/adminajax/createarticleform', admin.AjaxCreateFormHandler),
               ]