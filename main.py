import json
import datetime
from datetime import datetime, date, time
import pprint

program_version = 0.1
active_types = []
# TODO: How to handle the active types and stuff: if the list is empty, prompt the user after they make their selections for the day...

def launch():
    """Launches the program and loads user data into memory."""
    launch_text()
    if 
    global user_data
    user_data = json.load(open('user_data.txt'))
    if user_data['user_name'] == null:
        
    - Load all the JSON things
    today = datetime.today() <== datetime object 
    last_access = dictionary['last_access']
    if today > last_access:
        select_clothes()

def enter_user_name():
    
        
def launch_text():
    """Displays the program welcome message."""
    print("Welcome to 'Wardrobe'.")
    print("Version " + program_version + "\n")

def close():
    """Closes the program and exports the JSON data to file."""
    - json export with tabs from dictionary

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

def main():
    """Controls the execution of the program."""
    launch()
    
main()