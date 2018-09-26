from datetime import datetime
from random import randint
from time import sleep
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
# repeat the result three times
for i in range(3):

    right_this_minute = datetime.today().minute
    if right_this_minute in odds:
        print("This minute seems odd.")
    else:
        print("Not an odd minute.")
    today = datetime.today()
    if today == 'Saturday':
        print("Hurray!")
    elif today == 'Monday':
        print("Oh my God...")
    else:
        print("Just a usual day.")
    interval = randint(1, 60)
    sleep(interval)