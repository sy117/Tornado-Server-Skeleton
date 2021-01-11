
import tornado.web
from config import IS_DEVELOPMENT, SERVICE, API_VERSION
from routes.main_handler import MainHandler
from routes.error_handler import ErrorHandler
from routes.user_handler import UserHandler


def make_app():
    settings = {
        "debug": IS_DEVELOPMENT,
        "default_handler_class": ErrorHandler
    }
    return tornado.web.Application([
        ("/ping", MainHandler),
        ("/ping/", MainHandler),
        ("/{}/{}/users".format(SERVICE, API_VERSION), UserHandler),
        ("/{}/{}/users/".format(SERVICE, API_VERSION), UserHandler),
    ], **settings)
