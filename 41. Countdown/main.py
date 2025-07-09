# This Python code snippet is importing the `datetime` module and a custom module named
# `bday_messages`. It then calculates the number of days until a specific birthday date in 2025
# (August 31, 2025) from the current date.
import datetime, bday_messages  # from bday_messages import bday_messages

today = datetime.date.today()

next_birthday = datetime.date(2025, 8, 31)

days_away = time_difference = next_birthday - today

if today == next_birthday:
    print(bday_messages.random_message)
else:
    print(f"Your next birthday is in {days_away.days} days.")