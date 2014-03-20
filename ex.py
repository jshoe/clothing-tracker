import datetime
from datetime import datetime, date, time
import re
import json
import pprint
import calendar

def cal(year = date.today().year, month = date.today().month):
    """Displays and prints the current calendar to the user."""
    print("\n" + calendar.month(year, month) + "\n")

def check_quotes(user):
    """Checks the input for multiple string blocks."""
    if len(user) > 3:
        print_user_error()
        user_input()
        return

def split_quotes(user):
    """Splits the user input at quotes into pieces for processing."""
    user = user.split('"')
    check_quotes(user)
    return user

def print_input_error():
    """Prints an error message to the user."""
    print("\nUser input was invalid. Please try again.\n")

def date_okay(user):
    """Checks that the user-inputted date string is valid and returns it if true."""
    try:
        datetime(user[0], user[1], user[2], user[3], user[4])
    except ValueError:
        return False
    return user

def fill_date_blanks(user):
    """Changes dates like 3/17 to 2014-03-17. Also sets time to 00:01 if time is left blank."""
    if len(user) == 1:
        user.append(user[0])
        user[0] = date.today().month
    if len(user) == 2:
        user.append(user[1])
        user[1] = user[0]
        user[0] = date.today().year
    if len(user) == 3:
        user.append(0)
    if len(user) == 4:
        user.append(1)
    return user

def sanitize_check_date(user):
    """Sanitizes date inputs and returns them. Converts date to the format YYYY-MM-DD-HH-MM."""
    delimiter = re.search(r"(['/'])|-|(['.'])", user).group(0)
    user = user.split(delimiter)
    for x in range(len(user)):
        user[x] = int(re.sub(r'[^\d-]+', "", user[x]))
    user = fill_date_blanks(user)
    return date_okay(user)

def date_input_dispatch(user):
    """Interprets different kinds of dates, such as just a day of the month, a date like 3/17, or a date like 2014-03-17."""

    max_date = calendar.monthrange(date.today().year, date.today().month)[1]

    try:
        user = int(user)
        if 0 < user and user <= max_date:
            user = date_okay(fill_date_blanks([user]))
    except ValueError:
        user = sanitize_check_date(user)
    if not user:
        print_input_error()
        return enter_intended_start()
    return user

def date_list_to_str(user):
    new = ""
    for x in range(len(user)):
        new += ("-" + str(user[x]))
    return new[1:]

def enter_intended_start():
    """Fetches the intended start date of an item from the user and returns it in the format YYYY-MM-DD-HH-MM as a string."""
    cal()
    user = input("Enter intended start date as:\n(1) a numerical date in " + datetime.now().strftime("%B") + " (Example: 15),\n(2) a date this year (Example: 3/14), or\n(3) a specific date in the format YYYY-MM-DD, (Example: 2014-03-14).\n>>> ")
    user = date_input_dispatch(user)
    return date_list_to_str(user)
    
print(enter_intended_start())