import os
import json
from jsonschema import validate
from utils.logging_handler import Logger


# Decorator function
def validate_request(func):

    def json_schema_validation(*args, **kwargs):
        # write validaton logic here
        try:
            request = args[0].request
            request_body = json.loads(request.body)
            request_method = request.method.lower()
            schema_name = "{}_schema.json".format(request_method)
            # dirn = os.path.dirname(__file__)
            file_path = os.path.join(os.path.dirname(__file__), "schemas/{}".format(schema_name))
            Logger.info(file_path)
            with open(file_path) as schema:
                predefined_schema = json.loads(schema.read())
            validate(request_body, predefined_schema)
            func(*args, **kwargs)
        except Exception as error:
            return args[0].send_response(
                status=400, #bad request
                success=False,
                message=str(error)
            )
    
    return json_schema_validation



