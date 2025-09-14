import json
with open("restaurant.json", "r") as f:
    rest_data = json.load(f)
print(f" {rest_data['name']} is located at {rest_data['location']}, and serves {', '.join(rest_data['categories'])} cuisine.")

import menu
menu.describe_restaurant()
