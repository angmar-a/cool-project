class Restaurant:
    def __init__(self, name, location, categories):
        self.name = name
        self.location = location
        self.categories = categories

    def to_dict(self):
        return self.__dict__

    def describe(self):
        return f"{self.name} is located at {self.location}. It offers: {', '.join(self.categories)}"

restaurant_1 = Restaurant(
    "KAAKA",
    "One Lamplighter Way, Mail Center",
    ["Italian", "Popular & Organic", "Very delicioso"]
)
print(restaurant_1.describe())

while True:
    userinput = input("What would you like to do? view_menu_items, search_item, add_new_item, upload_existing_data, delete_item, or quit: ")
    from menu import MenuItem
    if userinput == 'view_menu_items':
        MenuItem.view_menu_items(MenuItem.data)
    elif userinput == 'search_item':
        MenuItem.search_item(MenuItem.data)
    elif userinput == 'add_new_item':
        MenuItem.add_new_item(MenuItem.data)
    elif userinput == 'upload_existing_data':
        MenuItem.upload_existing_data(MenuItem.data)
    elif userinput == 'delete_item':
        MenuItem.delete_item(MenuItem.data)
    elif userinput == 'quit':
        MenuItem.save_data_to_json(MenuItem.data)
        print("Data saved. Exiting program.")
        break
    else:
        print("Invalid input.")