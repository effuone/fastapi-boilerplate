# from datetime import datetime
# from typing import Optional

from bson.objectid import ObjectId
from pymongo.database import Database


class PostRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_post(self, input: dict):
        payload = {
            "city": input["city"],
            "message": input["message"],
            "user_id": ObjectId(input["user_id"])
        }

        self.database["posts"].insert_one(payload)

    def get_posts(self):
        return list(self.database["posts"].find({}))
    
    def get_post_by_id(self, post_id: str):
        return self.database["posts"].find_one({"_id": ObjectId(post_id)})
    
    def update_post(self, id: str, post: dict):
        self.database["posts"].update_one(
            filter={"_id": ObjectId(id)},
            update={
                "$set": post
            }
        )
    
    def delete_post(self, id: str):
        self.database["posts"].delete_one({"_id": ObjectId(id)})