"""Take:

Your birth year
Your friend's birth year
Current year

Calculate:

Both ages.
Age difference.
After how many years will one person become exactly twice as old as the other?

If it is impossible, print an appropriate message.

This question requires thinking before coding."""



birth_year = int(input("enter your birth year:"))
friend_year = int(input("enter your friends birth year:"))
current_year = int(input("enter the current year:"))

my_age = current_year - birth_year
friend_age = current_year - friend_year
age_difference = abs(my_age - friend_age)

print(f"my age is: {my_age}\nfrined age is: {friend_age}\nour age difference is :{age_difference}")

if my_age > friend_age:
    x = (2*friend_age - my_age)
    print(f"years left:{x}")
elif friend_age > my_age:
    x = (2*my_age - friend_age)
    print(f"years left:{x}")
else:
    print("an appropriate message")    

