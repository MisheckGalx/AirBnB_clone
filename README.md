#AirBnB_clone - Console


# Description of the project
The first part of this project involves simulating an Airbnb application by creating a control system for the modules used on our web page. We achieve this by implementing a JSON-format database and leveraging object-oriented programming, Python data translation, and command interpretation. The result is a local database that can be easily modified using specific commands, providing a flexible and efficient way to manage data.

# Installation
git clone https://github.com/MisheckGalx/AirBnB_clone.git; cd AirBnB_clone

# Run
./console.py or python3 console.py

# Testing
python3 -m unittest discover tests

# Prerequisites
sudo apt-get install python3

Use Available commands Command Explanation create Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel show Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234 all Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel update Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"

coded: Misheck Gogo and Brain Musakwa
