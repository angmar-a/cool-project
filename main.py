import json
with open("restaurant.json", "r") as f:
    rest_data = json.load(f)
print(rest_data)
import menu_item
print(rest_data['categories'])
menu_item.menu_item.view_menu_items(menu_item.menu_item.data)