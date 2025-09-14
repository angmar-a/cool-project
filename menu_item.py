class menu_item:
    import json
    file_path = None
    with open(f"cool-project/restaurant_data.json", "r") as file:
        data = json.load(file)

    def view_menu_items(data):
        for category in range(len(data['menu'])):
            print(f"\nCategory: {data['menu'][category]['category']}")
            for item in data['menu'][category]['items']:   
                print(f"\nMenu Item: {item['name']}; price: ${item['price']}; in stock: {item['in_stock']}; ID: {item['id']}")
    
    def search_item(data):
        item_id_to_find = int(input("Enter the item ID to search for: "))
        found_item = None
        for category in data["menu"]:
            for item in category["items"]:
                if item["id"] == item_id_to_find:
                    found_item = item
                    break  # Stop inner loop once found
                if found_item:
                    break  # Stop outer loop once found
                else:
                    print ("Item not found.")
                    break 

        if found_item:
            print(f"Found item with ID {item_id_to_find}: {found_item}")
        else:
            print(f"No item found with ID {item_id_to_find}")
    
    def add_new_item(data):
        new_item = {
            "id": input("What should the ID of the item be?"),  # Ensure this ID is unique
            "name": input ("Enter the name of the new item: "),
            "price": float(input("Enter the price of the new item: ")),
            "in_stock": input("Is the item in stock? (True/False): ").strip().lower() == 'true',
        }
        category = str(input("What category would you like to add the item to? appetizer/entree/dessert "))
        if category == 'appetizer':
            data['menu'][0]['items'].append(new_item)
        elif category == 'entree':
            data['menu'][1]['items'].append(new_item)
        elif category == 'dessert':
            data['menu'][2]['items'].append(new_item)
        else:
            print("Invalid category. Please choose from appetizer, entree, or dessert.")
            return
    
    def upload_existing_data(data):
       request = input ("What do you wnat to update? name/price/in_stock ")
       if request == 'name':
           item_id_to_update = int(input("Enter the item ID to update the name: "))
           new_name = input("Enter the new name: ")
           for category in data["menu"]:
               for item in category["items"]:
                   if item["id"] == item_id_to_update:
                       item["name"] = new_name
                       print(f"Item ID {item_id_to_update} name updated to {new_name}")
                       return
           print(f"No item found with ID {item_id_to_update}")
       elif request == 'price':
            item_id_to_update = int(input("Enter the item ID to update the price: "))
            new_price = float(input("Enter the new price: "))
            for category in data["menu"]:
                for item in category["items"]:
                    if item["id"] == item_id_to_update:
                        item["price"] = new_price
                        print(f"Item ID {item_id_to_update} price updated to {new_price}")
                        return
            print(f"No item found with ID {item_id_to_update}")
       elif request == 'in_stock':
            item_id_to_update = int(input("Enter the item ID to update the stock status: "))
            new_stock_status = input("Is the item in stock? (True/False): ").strip().lower() == 'true'
            for category in data["menu"]:
                for item in category["items"]:
                    if item["id"] == item_id_to_update:
                        item["in_stock"] = new_stock_status
                        print(f"Item ID {item_id_to_update} stock status updated to {new_stock_status}")
                        return
            print(f"No item found with ID {item_id_to_update}")

       else:
            print("Invalid request. Please choose from name, price, or in_stock.")
            return   

    def delete_item(data):
        item_id_to_delete = int(input("Enter the item ID to delete: "))
        for category in data["menu"]:
            for i, item in enumerate(category["items"]):
                if item["id"] == item_id_to_delete:
                    del category["items"][i]
                    print(f"Item ID {item_id_to_delete} has been deleted.")
                    return
        print(f"No item found with ID {item_id_to_delete}")


    def save_data_to_json(data):
        import json
        with open(f"cool-project/restaurant_data.json", "w") as file:
            json.dump(data, file, indent=4)
       
    #-----------------------------------------------------------------    

    #add_new_item(data)
    #save_data_to_json(data)


    #upload_existing_data(data)
    #add_new_item(data)
    #search_item(data)
    #delete_item (data)

    #view_menu_items(data)   

