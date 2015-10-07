import tornado.ioloop
import tornado.web
import os
import motor
class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('index.html')


if __name__ == "__main__":
    db = motor.MotorClient()
    
    application = tornado.web.Application(handlers=[
    (r'//static/(.*)', tornado.web.StaticFileHandler, {'path': './static'}),
    (r"/", MainHandler),
    (r'/bower_components/(.*)', tornado.web.StaticFileHandler, {'path': './bower_components'}),
    (r'/elements/(.*)', tornado.web.StaticFileHandler, {'path': './elements'}),
    (r'/elements/(.*)', tornado.web.StaticFileHandler, {'path': './elements'}),
    (r'/styles/(.*)', tornado.web.StaticFileHandler, {'path': './styles'}),
    (r'/scripts/(.*)', tornado.web.StaticFileHandler, {'path': './scripts'}),
    ],                                                                        
static_path=os.path.join(os.path.dirname(__file__), "static") ,db=db)
    port = 8889
    print 'Listening on http://localhost:', port
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()