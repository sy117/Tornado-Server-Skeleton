import tornado.ioloop
import tornado.httpserver
from config import IS_DEVELOPMENT, PORT
from utils.logging_handler import Logger
from routes import make_app



if __name__ == "__main__":
    app = make_app()
    if IS_DEVELOPMENT:
        app.listen(PORT)
        Logger.info("Development Server Running on :: http://0.0.0.0:{}".format(PORT))
    else:
        server = tornado.httpserver.HTTPServer(app)
        server.bind(PORT)
        Logger.info("Production Server Running on :: http://0.0.0.0:{}".format(PORT))
        server.start(0)
    tornado.ioloop.IOLoop.current().start()
