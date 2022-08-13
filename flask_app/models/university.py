from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class University:
    def __init__(self, data):
        self.id=data["id"]
        self.name=data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query="SELECT * FROM universities"
        result= connectToMySQL('tollkit_esquema').query_db(query)
        uni_arr=[]
        for i in result:
            uni_arr.append(cls(i))
        return uni_arr
