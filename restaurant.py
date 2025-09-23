import json

class Restaurant:
    def __init__(self, file_path):
        self.file_path = file_path

        with open(self.file_path, "r") as file:
            self.data = json.load(file)
            
        self.name = self.data["name"]
        self.location = self.data["location"]
        self.categories = self.data["menu"]

    def to_dict(self):
        return self.__dict__

    def describe(self):
        return f"{self.name} is located at {self.location}. It offers: {', '.join(self.categories)}"