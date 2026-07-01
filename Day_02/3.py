"""Create:
A list of 6 Fruits(with duplicate value)
convert into a set
convert the set into tuple
Then-
if the number of unique is greater than 4,print Good variety
otherwise print less variety
Also print all three data structure."""


Fruits = ["Banana","Apple","Orange","Mango","gold","jamun"]
set_1 = set(Fruits)
Tuple_1 = tuple(set_1)
print(set_1)
print(Tuple_1)
print(Fruits)
if (len(set_1)>4):
    print("Good variety")
else:
    print("Less variety")    