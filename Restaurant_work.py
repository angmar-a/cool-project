import json
class restaurant:
    def __init__(self, name, location, categories):
        self.name = name
        self.location = location
        self.categories = categories
    def to_json(self):
        return json.dumps(self.__dict__)
    def describe(self):
        print(f"{self.name} is located at {self.location} and serves {', '.join(self.categories)}.")
restaurant_1 = restaurant("KAAKA", "One lampligher way, mail center", ["Italian", "Popular & Organic", "Very delicioso"])
restaurant_1.describe()
    # Convert Python dict to JSON string
