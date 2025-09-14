import json
with open("restaurant.json", "r") as f:
    rest_data = json.load(f)
print(rest_data)

userinput=input("What would you like to do? view_menu_items, search_item, add_new_item, upload_existing_data, delete_item ")
import menu_item
if userinput == 'view_menu_items':
    menu_item.add_new_item(menu_item.data)
elif userinput == 'search_item':
    menu_item.search_item(menu_item.data)
elif userinput == 'add_new_item':
    menu_item.add_new_item(menu_item.data)
elif userinput == 'upload_existing_data':
    menu_item.upload_existing_data(menu_item.data)
elif userinput == 'delete_item':
    menu_item.delete_item(menu_item.data)
else:
    print("Invalid input")
    userinput=input("What would you like to do? view_menu_items, search_item, add_new_item, upload_existing_data, delete_item ")