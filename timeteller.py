"""
Python script that tells the time in words
"""

import datetime

#store the current time
now = datetime.datetime.now()

#store the hour, minute, and suffix
hour = now.hour
minute = now.minute
suffix = "AM"

#handle converting to 12 hour clock
if hour >= 12:
    suffix = "PM"
    hour -= 12

#handle hour 0
if hour == 0:
    hour = 12

#list of time units and their names
time_units = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "quarter",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty"
}

#handle minutes of 0
if minute == 0:
    print(time_units[hour] + " o'clock " + suffix)
#handle minutes < 20
elif minute < 20:
    print(time_units[hour] + " " + time_units[minute] + " " + suffix)
#handle minutes > 20
else:
    #find the tens digit
    tens = int(minute / 10)
    #find the ones digit
    ones = int(minute % 10)
    if ones == 0:
        print(time_units[hour] + " " + time_units[tens * 10] + " " + suffix)
    else:
        print(time_units[hour] + " " + time_units[tens * 10] + " " + time_units[ones] + " " + suffix)