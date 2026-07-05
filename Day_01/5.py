"""take the user input like 
name
birth year
current year
calculate:-current age,age after 25 years,age before 10 years """


name = input("What is your name :")
birth_year = int(input("enter your birth year:"))
current_year = int(input("enter the current year:"))
current_age = (current_year - birth_year)
Age_25 = (current_age + 25)
Age_10 = (current_age - 10)
print(f"your current age is {current_age} and you will be {Age_25} years will be old after 25 years and you were {Age_10} years old before 10 years")