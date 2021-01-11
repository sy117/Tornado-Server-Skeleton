''' Utility methods for performing database operations '''

''' Trying to mimic a actual database server '''

import uuid


users = [
    {
        "_id": "7a7f4f7f-19fb-4266-b1cf-666158cf17fb",
        "first_name":"Virat",
        "last_name": "Kohli",
        "email": "imvk@gmail.com"
    },
    {
        "_id": "e4dc6add-956e-4bc5-8122-047ef2ca42e3",
        "first_name":"Rohit",
        "last_name": "Sharma",
        "email": "hitman@gmail.com"
    },
    {
        "_id": "b6b66d84-6aff-4c7a-9897-775920e76787",
        "first_name":"Jasprit",
        "last_name": "Bumrah",
        "email": "boomboom@ggmail.com"
    },
    {
        "_id": "ae21491d-d7fc-498d-b2f9-5f6d015a62b8",
        "first_name":"Ajinkya",
        "last_name": "Rahane",
        "email": "merahane@gmail.com"
    }
]


def get_all_users():
    return users



def get_user_by_id(user_id):
    filtered_usres = list(filter(lambda obj: obj["_id"] == user_id, users))
    if len(filtered_usres) > 0:
        return filtered_usres[0]
    raise Exception("Invalid User Id")


def add_user(user_details):
    user_id = str(uuid.uuid4())
    user = {
        "_id": user_id,
        ** user_details
    }
    users.append(user)
    return user

def update_user(updated_details):
    user_id = updated_details["_id"]
    del updated_details["_id"]
    index = -1
    for i in range(len(users)):
        if user_id == users[i]["_id"]:
            index = i
            break
    if index == -1:
        raise Exception("No user found with given Id")
    user = users[index]
    for key in updated_details:
        user[key] = updated_details[key]
    users[index] = user
    return user
