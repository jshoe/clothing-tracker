import json
from datetime import datetime, date, time
import pprint

program_version = 0.1

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
            i -= 1
        if self.soil_count == 0:
            self.is_clean = True


def string_to_date(date):
    """Converts a string in the format YYYY-MM-DD to a datetime object."""
    date = date.split('-')
    return datetime(int(date[0]), int(date[1]), int(date[2]))


def date_to_string(date):
    """Converts a datetime object to a string in the format YYYY-MM-DD."""
    return date.strftime('%Y-%m-%d')


def add_daily_types(all_types, daily_types):
    """Allows the user to specify more daily types."""
    print("\nHere is a list of clothing types found in your inventory:\n")
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
    def launch_text():
        """Displays the program welcome message."""
        print("Welcome to 'Wardrobe'.")
        print("Version " + str(program_version) + "\n")

    def greet_user():
        """Prompts the user for a name if not stored, and then greets them."""
        nonlocal data
        try:
            name = data['user_name']
            if (name == None) or (name == ''): # check if this will even generate a KeyError
                name = input("Please enter your name:\n>>> ")
        except KeyError as e:
            name = input("Please enter your name:\n>>> ")
        print("Hello there, " + name + ".")
        return name

    def set_daily_types():
        """Returns the daily types of clothing items from the database, or prompts the user to select them first."""
        def make_types_list(items):
            """Makes a list of all the types of clothing found in the database."""
            all_types = []
            for i in items:
                if (i['type'] not in all_types) and (i['type'] != ""):
                    all_types.append(i['type'])
            return all_types

        nonlocal data
        daily_types = []

        try:
            daily_types = data['daily_types']
        except KeyError as e:
            all_types = make_types_list(data['items'])
            if len(all_types) == 0:
                return
            else:
                daily_types = add_daily_types(all_types, daily_types)
        return daily_types

    def exit():
        """Exports the user data to a text file in JSON and exits."""
        nonlocal data
        nonlocal daily_types
        nonlocal inventory

        data['daily_types'] = daily_types
        items = []
        for i in inventory:
            dict = {"type": i.type, "message": i.message, "details": i.details, "worn": i.worn, "washed": i.washed}
            items.append(dict)
        data['items'] = items

        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile, indent = 2, sort_keys = True)

    launch_text()

    try:
        data = json.load(open('data.txt'))
    except IOError:
        data = {"program_version": program_version, "user_name": "", "updated_time": date.today().strftime('%Y-%m-%d'), "daily_types": [ ], "items": [ ]}

    daily_types = set_daily_types()

    inventory = []
    for i in data['items']:
        inventory.append(Item(i))

    data['user_name'] = greet_user()

    updated_time = data['updated_time']
    exit()
    
launch()