import tornado
import json

class BaseHandler(tornado.web.RequestHandler):


    def set_default_headers(self):
        self.set_header("Content-type", "application/json")
    

    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass
    
    def delete(self):
        pass
    
    def send_response(self, success=True, status=200, message="", response=None):
        self.set_status(status)
        return self.write(json.dumps({
            "success": success,
            "message": message,
            "data": response
        }))