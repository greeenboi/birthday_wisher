import os
from datetime import datetime
from dotenv import load_dotenv

class BirthdayChecker:
    def __init__(self):
        load_dotenv()
        self.birthday_list = os.getenv('BIRTHDAY_LIST', '')

    def check_birthdays(self):
        current_date = datetime.now().strftime("%d/%m")
        
        records = self.birthday_list.split('\n')
        
        for record in records:
            if record.strip(): 
                name, bday = record.split(',')
                bday_month_day = datetime.strptime(bday, "%d/%m/%y").strftime("%d/%m")
                if bday_month_day == current_date:
                    print(f"Today is {name}'s birthday!")

if __name__ == "__main__":
    checker = BirthdayChecker()
    checker.check_birthdays()