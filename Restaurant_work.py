import json

class Restaurant:
    def __init__(self, name, location, categories):
        self.name = name
        self.location = location
        self.categories = categories

    def to_dict(self):
        return self.__dict__



# Save to a JSON file
with open("restaurant.json", "w") as f:
    json.dump(restaurant_1.to_dict(), f, indent=4)
