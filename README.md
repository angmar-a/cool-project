# cool-project
Project description: 
This project offers a description of the restaurant, including its name, location, and several characteristics. It allows the user to input one of the five functions it offers: they can view the entire list of menu, add new items, delete an item, search for an item, or change any traits of an item using a while True loop. That is, unless the user inputs "quit", the program will continuously ask for user input. If the user chooses to input one of the functions, the changes will be saved permanently in the json file, if not, the program will say: invalid input. 
Sample interaction:
What would you like to do? view_menu_items, search_item, add_new_item, upload_existing_data, delete_item, or quit: add_new_item
What should the ID of the item be?4
Enter the name of the new item: Mango Sago
Enter the price of the new item: 4.22
Is the item in stock? (True/False): True
What category would you like to add the item to? appetizer/entree/dessert dessert
What would you like to do? view_menu_items, search_item, add_new_item, upload_existing_data, delete_item, or quit: delete_item
Enter the item ID to delete: 4
Item ID 4 has been deleted.
What would you like to do? view_menu_items, search_item, add_new_item, upload_existing_data, delete_item, or quit: view_menu_items

Category: Appetizer

Menu Item: Spring Rolls; price: $5.99; in stock: True; ID: 1

Menu Item: Chicken Satay; price: $7.49; in stock: True; ID: 2

Menu Item: Fried Tofu; price: $6.49; in stock: True; ID: 3

Menu Item: Papaya Salad; price: $7.99; in stock: True; ID: 5

Menu Item: Crispy Wontons; price: $6.99; in stock: True; ID: 6

Menu Item: Tom Yum Soup (Cup); price: $5.49; in stock: True; ID: 7

Menu Item: Edamame (Spicy); price: $6.49; in stock: False; ID: 8

Category: Entree

Menu Item: Pad Thai; price: $13.99; in stock: True; ID: 9

Menu Item: Drunken Noodles; price: $14.49; in stock: True; ID: 10

Menu Item: Green Curry; price: $15.49; in stock: True; ID: 11

Menu Item: Red Curry; price: $15.49; in stock: True; ID: 12

Menu Item: Massaman Curry; price: $16.99; in stock: True; ID: 13

Menu Item: Panang Curry; price: $15.99; in stock: True; ID: 14

Menu Item: Thai Fried Rice; price: $12.99; in stock: True; ID: 15

Menu Item: Basil Chicken (Pad Kra Pao); price: $14.99; in stock: True; ID: 16

Menu Item: Cashew Nut Chicken; price: $15.49; in stock: True; ID: 17

Menu Item: Grilled Lemongrass Salmon; price: $18.99; in stock: False; ID: 18

Menu Item: Pad See Ew; price: $14.45; in stock: True; ID: 19

Menu Item: tre; price: $3456.0; in stock: True; ID: 345

Menu Item: hh; price: $88789.0; in stock: False; ID: 88

Category: Dessert

Menu Item: Mango Sticky Rice; price: $7.99; in stock: True; ID: 20

Menu Item: Fried Banana with Honey; price: $6.49; in stock: True; ID: 21

Menu Item: Thai Coconut Ice Cream; price: $5.99; in stock: True; ID: 22

Menu Item: Pumpkin Custard; price: $6.99; in stock: False; ID: 23

Menu Item: Mango Sago; price: $4.22; in stock: True; ID: 4
What would you like to do? view_menu_items, search_item, add_new_item, upload_existing_data, delete_item, or quit: quit
Data saved. Exiting program.
Set-up & Run instructions:
1.Install Python & Visual Studio Code 
2.Clone this repository 
3.Open the cloned file in VS code 
4.Cool-project->main->run
5.Using the program and provide input
    -Follow the instructions 
    -To quit, enter "quit"

File structure: 
This project is based on three major files: restaurant_work, a dictionary that introduces a list of description of the restaurant; menu.py, a class that contains the definition of 5 functions: view, add, upload, search, and delete; and resaurant_data, a json file that stores the dishes of the restaurant as the user updates the menu. Both menu and restaurant_work is imported into the main file. 