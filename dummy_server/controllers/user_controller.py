''' Utility methods to control business logic '''

from utils.logging_handler import Logger
from services.db_service import get_user_by_id, get_all_users, add_user, update_user



def fetch_user(request_args):
    # write core logic here
    if "user_id" in request_args:
        user_id = request_args["user_id"][0].decode("utf-8")
        Logger.info("user_id:: {}".format(user_id))
        return get_user_by_id(user_id)
    return get_all_users()


def create_user(request_body):
    # write core logic here if required
    return add_user(request_body)


def modify_user_details(request_body):
    # write core logic here
    if "_id" not in request_body:
        raise Exception("Id is a required property in request body!")
    return update_user(request_body)


