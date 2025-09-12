import json
with open('Restaurant_work.py', "r") as file:
    rest_data = json.load(file)
    
print(rest_data['name'])