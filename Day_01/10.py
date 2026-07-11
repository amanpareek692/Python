"""A water tank has dimensions:

Length
Width
Height

Input dimensions in meters.

Find:

Volume in cubic meters.
Convert the volume into liters.

(1 cubic meter = 1000 liters)

Also calculate:

If one person uses 150 liters/day, for how many days can the tank supply water?

Round the answer to 1 decimal place."""

import math

length = int(input("enter the length in m:"))
breadth = int(input("enter the breadth in m:"))
height = int(input("enter the height in m:"))

volume = length*breadth*height
litres = volume*1000
daily_litre = litres/150
daily_litre = round(daily_litre,1)

print(volume,"m^3")
print(litres,"L")
print(daily_litre,"L")

