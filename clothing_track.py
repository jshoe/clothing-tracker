import json
from datetime import datetime, date, time

def to_date(string):
    """Converts a string in the format YYYY-MM-DD to a datetime object."""
    return datetime.strptime(string, '%Y-%m-%d')

def to_strng(date):
    """Converts a datetime object to a string in the format YYYY-MM-DD."""
    return date.strftime('%Y-%m-%d')

def launch():
    """Launches the program and loads user data from text file into memory."""
    print("\n\nWelcome to the clothing tracking program. The day is " + datetime.now().strftime('%Y-%m-%d') + ".")
    data = json.load(open('data.txt'))
    data['items'] = parse_dates(data['items'])
    main_screen(data)

def min_soil(items, type):
    """Finds the minimum soil count among the items of the specified clothing type."""
    min_soiled = 9999
    for i in items: #finds the min soil_count
        if i['type'] != type:
            continue
        if i['location'] != 'Shelf':
            continue
        cur = soil_count(i)
        if cur < min_soiled:
            min_soiled = cur
    return min_soiled

def best(items, type):
    """Selects the optimal item of clothing of the specified type from the given items."""
    # Setting the default first item
    n = 0
    for i in items:
        if i['type'] != type:
            n += 1
    temp_best = items[n] #default value

    # Selecting for the item that hasn't been worn in the longest time
    oldest_so_far = datetime(9999, 1, 1)
    for i in items:
        if i['type'] != type:
            continue
        if i['location'] == 'Laundry basket':
            continue
        if soil_count(i) > min_soil(items, type): #soil_count takes priority
            continue
        try:
            today = datetime.now().strftime('%Y-%m-%d')
            if today in i['skip_days']:
                continue
        except:
            pass
        cur = to_date(max(i['worn']))
        if cur < oldest_so_far:
            oldest_so_far = cur
            temp_best = i

    return temp_best

'''def oldest_wear_logic(items, min_soiled, temp_best):
    # Selecting for the item that hasn't been worn in the longest time
    oldest_so_far = datetime(9999, 1, 1)
    for i in items:
        if i['type'] != type:
            continue
        if i['location'] == 'Laundry basket':
            continue
        if soil_count(i) > min_soiled: #soil_count takes priority
            continue
        try:
            today = datetime.now().strftime('%Y-%m-%d')
            if today in i['skip_days']:
                continue
        except:
            pass
        cur = to_date(max(i['worn']))
        if cur < oldest_so_far:
            oldest_so_far = cur
            temp_best = i
    return temp_best'''

def display_target(target, data):
    """Prints out a string for the currently selected item of clothing."""
    for i in data['items']:
        if i['id_num'] != target:
            continue
        print("\nSELECTED: " + i['brand'] + " " + i['color'] + " " + i['message'] + " " + i['style'])

def recommend(best_top, best_shorts, best_pants):
    """Prints the recommended items of clothing."""
    print("\nNOTES:")
    print("* Picked by the least # of soiled wears, followed by the last wear date.")
    print("* 'L' indicates that the item is currently in the laundry basket.")
    print("\nRECOMMENDED TOP:\n  - " + best_top['brand'] + " " + best_top['color'] + " " + best_top['message'] + " " + best_top['style'] + ".")
    print("\nRECOMMENDED SHORTS:\n  - " + best_shorts['brand'] + " " + best_shorts['color'] + " " + best_shorts['message'] + " " + best_shorts['style'] + ".")
    print("\nRECOMMENDED PANTS:\n  - " + best_pants['brand'] + " " + best_pants['color'] + " " + best_pants['message'] + " " + best_pants['style'] + ".")
    #print("\nRECOMMENDED OUTERWEAR:\n  - " + best_outerwear['brand'] + " " + best_outerwear['color'] + " " + best_outerwear['message'] + " " + best_outerwear['style'] + ".")

def input_err():
    """Displays generic input error message to the user."""
    print("\nSorry, not a valid input. Please try again.\n")

def days_left(data, fav):
    """Calculates remaining days of clean clothes left for the user."""
    days_left = 0
    print("- Days before running out of " + fav + ": ", end = "")
    for i in data['items']:
        if i['type'] != fav or i['location'] != 'Shelf':
            continue
        count = soil_count(i)
        if count < 3:
            days_left += (3 - count)
    print(days_left)

def skip_item(data, target):
    """Flags the target item of clothing to skip for wearing today."""
    for i in data['items']:
        if i['id_num'] == target:
            try:
                today = datetime.now().strftime('%Y-%m-%d')
                if today in i['skip_days']:
                    continue
                i['skip_days'].extend([today])
            except KeyError:
                i['skip_days'] = list([today])
    return data

def print_main_options():
    """Shows the user the options for the main screen."""
    print("\nOPTIONS:")
    print("(AS) - Accept the recommended shirt and shorts and mark both as worn today")
    print("(AP) - Accept the recommended shirt and pants and mark both as worn today")
    print("(NT) - Skip the current recommended top and pick the next top")
    print("(NS) - Skip the current recommended shorts and pick the next shorts")
    print("(NP) - Skip the current recommended pants and pick the next pants")
    print("(WQ) - Save current data and quit the program")
    print("(Q) - Exit the program without saving changes")
    print("(#) - Enter the number of an item to select")

def main_screen(data):
    """Prints the clothing collection and manages user action."""    
    id_list = print_inventory(data['items'])
    best_top = best(data['items'], 'Shirt')
    best_shorts = best(data['items'], 'Shorts')
    best_pants = best(data['items'], 'Pants')
    print("")
    days_left(data, 'Shirt')
    days_left(data, 'Shorts')
    days_left(data, 'Pants')
    recommend(best_top, best_shorts, best_pants)

    ok = False
    while not ok: #before selecting an item of clothing
        print_main_options()
        choice = input("\n>>> ")
        if not choice.strip():
            input_err()
            continue        
        choice = choice.lower()
        if choice == 'as':
            data = wear_today(data, best_top['id_num'])
            data = wear_today(data, best_shorts['id_num'])
            main_screen(data)
            return
        elif choice == 'ap':
            data = wear_today(data, best_top['id_num'])
            data = wear_today(data, best_pants['id_num'])
            main_screen(data)
            return
        elif choice == 'q':
            return
        elif choice == 'wq':
            exit(data)
            return
        elif choice == 'nt':
            data = skip_item(data, best_top['id_num'])
            main_screen(data)
            return
        elif choice == 'ns':
            data = skip_item(data, best_shorts['id_num'])
            main_screen(data)
            return
        elif choice == 'np':
            data = skip_item(data, best_pants['id_num'])
            main_screen(data)
            return

        try:
            target = int(choice)
        except:
            input_err()
            continue
        if (target >= 1) and (target <= len(data['items'])):
            ok = True
        else:
            input_err()

    main_screen(item_options(data, id_list[target - 1]))

def print_item_options():
    """Shows the user the options for a selected item of clothing."""
    print("\nOPTIONS:")
    print("(L) - Move the item to the laundry basket")
    print("(W) - Mark the item as worn today")
    print("(C) - Mark the item as cleaned today")
    print("(X) - Cancel and de-select the current item")
    
def item_options(data, target):
    """Shows options and takes user input on actions for currently selected item."""
    display_target(target, data)
    ok = False
    while not ok: #while selecting an item of clothing
        print_item_options()
        choice = input("\n>>> ")
        if not choice.strip():
            input_err()
            continue
        choice = choice.lower()
        if choice == 'x':
            main_screen(data)
            return 
        elif choice == 'l':
            data = to_basket(data, target)
            ok = True
        elif choice == 'w':
            data = wear_today(data, target)
            ok = True
        elif choice == 'c':
            data = wash_today(data, target)
            ok = True
        else:
            input_err()
    return data

def wash_today(data, target):
    """Marks the target item of clothing as washed."""
    for i in data['items']:
        if i['id_num'] == target:
            i['washed'].append(datetime.now().strftime('%Y-%m-%d'))
            i['location'] = 'Shelf'
            print("\nItem successfully marked as washed today.")
    return data

def to_basket(data, target):
    """Marks the target item of clothing as in the laundry basket."""
    for i in data['items']:
        if i['id_num'] == target:
            i['location'] = 'Laundry basket'
            print("\nItem successfully moved to laundry basket.")
    return data

def wear_today(data, target):
    """Marks the target item of clothing as worn today."""
    today = datetime.now().strftime('%Y-%m-%d')

    for i in data['items']:
        if i['id_num'] == target:
            if today in i['worn']:
                return data
            i['worn'].extend([today])
            print("\nItem successfully marked as worn today.")

    return data

def parse_dates(items):
    """Converts all dates in the list of items to datetime format and sorts dates."""
    for i in items:
        for j in i['washed']:
            j = to_date(j)
        for k in i['worn']:
            k = to_date(k)
        i['washed'].sort()
        i['worn'].sort()
    return items

def print_favs(fav, items, id_list, num):
    """Prints all the items in the specified category and details about each item."""
    print("\n" + fav + ":\n")

    for i in items:
        if i['type'] != fav:
            continue
        print("(", end="")
        if num < 10:
            print("0", end="")
        print(str(num) + ") " + max(i['worn']) + " | ", end="")
        if i['location'] == 'Laundry basket':
            print("L", end="")
        else:
            print(str(soil_count(i)), end="")
        print(" | " + i['brand'] + " " + i['color'] + " " + i['message'] + " " + i['style'])
        id_list.extend([i['id_num']])
        num += 1
    return (id_list, num)

def print_inventory(items):
    """Prints the user's current inventory of clothing."""
    id_list = []
    num = 1
    
    print("\nLAST WEAR - SOIL COUNT - ITEM INFO:")

    id_list, num = print_favs('Shirt', items, id_list, num)
    id_list, num = print_favs('Shorts', items, id_list, num)
    id_list, num = print_favs('Pants', items, id_list, num)

    return id_list

def soil_count(item):
    """Calculates a soil count for the item of clothing."""
    last_wash = max(item['washed'])
    if last_wash >= max(item['worn']):
        return 0
    soil_count = 0
    prev = -1
    for i in item['worn']:
        if i == prev:
            continue
        elif i > last_wash:
            soil_count += 1
        prev = i
    return soil_count

def exit(data):
    """Exports the user data to a text file in JSON and exits."""
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile, indent = 2, sort_keys = True)
    return

launch()