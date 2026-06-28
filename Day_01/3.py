"""Take a Decimal Number as input From the user.
Print
Interger value
rounded value
data type before conversion
data type after converting to an integer"""


Decimal_number=(input("Enter THe Decimal Value:"))
print(int(float(Decimal_number)))
print(round(float(Decimal_number)))
print(type(Decimal_number))
print(type(int(float(Decimal_number))))