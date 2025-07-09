# This block of code in Python is creating a list `bday_messages` containing different birthday
# messages. It then imports the `random` module to select a random message from the list using the
# `random.choice()` function and assigns it to the variable `random_message`. This allows for a random
# birthday message to be selected and displayed each time the code is run.
import random

bday_messages = ['Hope you have a very Happy Birthday! 🎈',
'Its your special day – get out there and celebrate! 🎉',
'You were born and the world got better – everybody wins! 🥳',
'Have lots of fun on your special day! 🎂',
'Another year of you going around the sun! 🌞']

random_message = random.choice(bday_messages)