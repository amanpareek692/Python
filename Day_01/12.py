"""A phone has:

Battery percentage now
Battery drain per hour

Calculate:

How many hours the battery will last.
Convert that time into:
Hours
Minutes

Example:
Battery = 73%
Drain = 18% per hour.

How long until battery reaches 0%?"""

battery_percentage = int(input("enter the batter percentage:"))
battery_drain = int(input("enter the battery drain per hour:"))
if battery_drain == 0:
    print("battery will never drain")
else:
    hours_left = (battery_percentage/battery_drain)
    minutes_left = round((hours_left*60)%60)
    hours = int(hours_left)

    print(f"battery will drain in:{hours} hours {minutes_left} minutes")

  

