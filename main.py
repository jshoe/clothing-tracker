import json
import datetime
from datetime import datetime, date, time
import pprint

program_version = 0.1
active_types = []
# TODO: How to handle the active types and stuff: if the list is empty, prompt the user after they make their selections for the day...
# TODO: Parse through the JSON file and make a list of all the valid types.

class Item:
    """An item of clothing."""
    
    def __init__(self, data):
        self.type = data['type']
        self.message = data['message']
        self.details = data['details']
        self.worn = data['worn']
        self.last_worn = self.worn[-1]
        self.washed = data['washed']
        self.last_washed = data['washed'][-1]
        if 

def launch():
    """Launches the program and loads user data into memory."""
    launch_text()
    data = json.load(open('data.txt')) # TODO: make the data.txt file if not there
    
    inventory = []
    for i in range(len(data['items'])):
        inventory.append(Item(data['items'][i]))

    greet_user()

    today = datetime.today() <== datetime object 
    last_access = dictionary['last_access']
    if today > last_access:
        select_clothes()
    exit()

def greet_user():
    """Prompts the user for a name if not stored, and then greets them."""
    nonlocal data
    try:
        name = data['user_name']
        if (name == None) or (name == ''): # check if this will even generate a KeyError
            name = input("Please enter your name:\n>>> ")
    except KeyError, e:
        name = input("Please enter your name:\n>>> ")
    print("Hello there, " + name + ".")

def launch_text():
    """Displays the program welcome message."""
    print("Welcome to 'Wardrobe'.")
    print("Version " + program_version + "\n")
    
def exit():
    """Exports the user data to a text file in JSON and exits."""
    nonlocal data
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile, indent = 2, sort_keys = True)

def main_display():
    """Shows the main display of clothing display."""
    #, ITEM, BRAND, WORN_COUNT
    for item in dictionary_entry:
        pprint(item, brand, worn_count)

def select_clothes():
    """Will select your clothing for the day and ask you which you picked."""

def command_dispatch(user):
    if "accept" in user:
    elif "shuffle" in user:
    elif "exit" in user:
    else:
        error handling
    ^ Actually, we're not even using this since the new scheme will be all numbers-based.

def clothes_selection():
    """Handles the clothing selection algorithm."""
    
def select_clothes_menu_text():
    """Displays command options for the user."""
    # TODO: This menu should not be like hard-coded... they should be able to pick as many pieces of clothing that they want.
    print("\nEnter the # of a command.")
    print("[1] Accept outfit and mark as worn for the day.")

    
    print("[2] Reshuffle outfit and select a new one.")
    print("[3] Reshuffle bottom and select a new one.")
    print("[4] Reshuffle top and select a new one.")
    print("[5] Return to Main Menu.\n")

launch()