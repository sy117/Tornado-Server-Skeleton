from routes.base_handler import BaseHandler


class MainHandler(BaseHandler):

    def get(self):
        return self.send_response(
            message="Successfully reached Backend API!!"
        )