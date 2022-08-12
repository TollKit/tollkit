

class University:
    def __init__(self, data):
        self.id=data["id"]
        self.name=data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]