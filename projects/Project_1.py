import random

"""0 is for rock
   1 is for paper
   2 is for scissor"""


user_choice = int(input("enter the choice between 0,1,2:"))
computer_choice = (random.randint(0,2))
print(computer_choice)

if ((user_choice > computer_choice)or(user_choice == 0 and computer_choice == 2)):
    print("you win")
elif ((computer_choice > user_choice)or(user_choice == 2 and computer_choice == 0)):
    print("you lose") 
else:
    print("draw")
