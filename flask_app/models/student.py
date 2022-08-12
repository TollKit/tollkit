

class Student:
    def __init__(self, data):
        self.id=data["id"]
        self.name=data["name"]
        self.lastname=data["lastname"]
        self.temp=data["temp"]
        self.has_mask=data["has_mask"]
        self.has_studentCard=data["has_studentCard"]
        self.has_alcohol=data["has_alcohol"]
        self.has_covidCard=data["has_covidCard"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
