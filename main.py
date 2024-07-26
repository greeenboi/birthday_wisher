import os
from datetime import datetime
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

def check_birthdays(birthday_list):
    # Get the current date in month-day format
    current_date = datetime.now().strftime("%d/%m")
    
    # Split the birthday list into individual records
    records = birthday_list.split('\n')
    
    # Iterate through the records
    for record in records:
        if record.strip():  # Skip empty lines
            name, bday = record.split(',')
            # Extract month and day from the birthday
            bday_month_day = datetime.strptime(bday, "%d/%m/%y").strftime("%d/%m")
            # print(f"Checking birthday for {name}")
            # print(bday_month_day)
            # Check if the current date matches the birthday
            if bday_month_day == current_date:
                print(f"Today is {name}'s birthday!")

# Get the BIRTHDAY_LIST from the .env file
birthday_list = os.getenv('BIRTHDAY_LIST', '')

# print(birthday_list)

# Check birthdays
check_birthdays(birthday_list)