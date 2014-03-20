import json
import datetime
from datetime import datetime, date, time
import pprint

program_version = 0.1
# TODO: Parse through the JSON file and make a list of all the valid types.
# TODO: A method for people to input clothing into the database / imoprt their clothing collection :P. Along with a delete and modify function.
# TODO: Need to find a way to like go back from these init fields and turn back into a dictionary for the JSON export...
# TODO: Add lots of "input" error control.
# TODO: Tidy up use of the nonlocal statement :P.

class Item:
    """An item of clothing."""
    
    def __init__(self, data):
        """Creates an item of clothing with all its characteristics."""
        self.type = data['type']
        self.message = data['message']
        self.details = data['details']
        self.worn = data['worn']
        self.last_worn = self.worn[-1]
        self.washed = data['washed']
        self.last_washed = data['washed'][-1]
        self.soil_count = 0
        i = -1
        while i >= -len(self.worn):
            if string_to_date(self.last_washed) < string_to_date(self.worn[i]):
                self.soil_count += 1
            elif string_to_date(self.worn[i]) < string_to_date(self.last_washed):
                break
            i--
        if self.soil_count == 0:
            self.is_clean = True

def string_to_date(date):
    """Converts a string in the format YYYY-MM-DD to a datetime object."""
    date = date.split('-')
    return datetime(date[0], date[1], date[2])

def date_to_string(date):
    """Converts a datetime object to a string in the format YYYY-MM-DD."""
    return date.strftime('%Y-%m-%d')

def add_daily_types(all_types, daily_types):
    """Allows the user to specify more daily types."""
    print("\nHere is a list of clothing types found in your inventory:\n");
    j = 1
    for i in all_types:
        print("[" + j + "] " + i)
        j += 1
    print("\nEvery day that you open the program, the program will automatically ")
    print("select items of clothing from your 'daily' clothing types.")
    print("\nSet these 'daily' clothing types now by typing in their corresponding")
    print("numbers, separated by commas, e.g. '2, 4, 5'.\n")
    set_list = input()
    set_list = set_list.split(",")
    for j in set_list:
        j = j.lstrip(' ')
        daily_types.append(all_types[j - 1])
    return daily_types
    
def launch():
    """Launches the program and loads user data into memory."""
    launch_text()
    data = json.load(open('data.txt')) # TODO: make the data.txt file if not there
    
    inventory = []
    for i in data['items']:
        inventory.append(Item(i))

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
        return name

    def set_daily_types():
        """Returns the daily types of clothing items from the database, or prompts the user to select them and then returns them."""
        nonlocal data

        def make_types_list(items):
            """Makes a list of all the types of clothing found in the database."""
            all_types = []
            for i in items:
                if (i['type'] not in all_types) and (i['type'] != ""):
                    all_types.append(i['type'])
            return all_types

        daily_types = []
            
        try:
            daily_types = data['daily_types']
        except KeyError, e:
            all_types = make_types_list(data['items'])
            if len(all_types) == 0:
                return 
            else:
                daily_types = add_daily_types(all_types, daily_types)
        return daily_types

    data['user_name'] = greet_user()
        
    daily_types = set_daily_types()

    updated_time = data['updated_time']
    if string_to_date(updated_time) < datetime.today():
        select_clothes()
    exit()

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