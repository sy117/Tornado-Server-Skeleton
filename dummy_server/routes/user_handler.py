import json
from routes.base_handler import BaseHandler
from controllers.user_controller import fetch_user, create_user, modify_user_details
from middlewares.request_validation import validate_request

class UserHandler(BaseHandler):

    def get(self):
        try:
            self.send_response(
                message="Data fetched successfully!",
                response=fetch_user(self.request.arguments)
            )
        except Exception as error:
            self.send_response(
                success=False,
                status=500,
                message=str(error)
            )

    @validate_request
    def post(self):
        try:
           self.send_response(
               message="User added successfully!",
               response=create_user(json.loads(self.request.body))
            ) 
        except Exception as error:
            
            self.send_response(
                success=False,
                status=500,
                message=str(error)
            )
    
    def put(self):
        try:
            self.send_response(
                message="User data updated successfully!",
                response=modify_user_details(json.loads(self.request.body))
            ) 
        except Exception as error:
            self.send_response(
                success=False,
                status=500,
                message=str(error)
            )