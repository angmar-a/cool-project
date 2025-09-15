# cool-project
Project description: 

This project offers a description of the restaurant, including its name, location, and several characteristics. It allows the user to input one of the five functions it offers: they can view the entire list of menu, add new items, delete an item, search for an item, or change any traits of an item using a while True loop. That is, unless the user inputs "quit", the program will continuously ask for user input. If the user chooses to input one of the functions, the modifications will be seen (whether they want to add an item, change an existing one, etc.) In any other case, the program will state invalid input. Besides that, user can always save teh changes to the original json file (it is a separate function)

Set-up & Run instructions:

1.Install Python & Visual Studio Code 
2.Clone this repository 
3.Open the cloned file in VS code 
4.Cool-project->main->run
5.Using the program and provide input
    -Follow the instructions 
    -To quit, enter "quit"

Example of input and output iteraction: 






File structure: 
This project is based on three major files: restaurant_work, a dictionary that introduces a list of description of the restaurant; menu.py, a class that contains the definition of 5 functions: view, add, upload, search, and delete; and resaurant_data, a json file that stores the dishes of the restaurant as the user updates the menu. Both menu and restaurant_work is imported into the main file. 
