from routes.base_handler import BaseHandler

class ErrorHandler(BaseHandler):

    def prepare(self):

        return self.send_response(
            status=404,
            success=False,
            message="Resource not found!",   
        )