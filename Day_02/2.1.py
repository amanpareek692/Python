"""Take input for
Age
Indian citizen(yes/no)
Has voter id(yes/no)
Rules:
if age is at least 18:
Check if the user is an indian citizen.
if yes,check if they have voter id.
if yes,print Eligible for vote.
otherwise,print apply for Voter id.
if not an indian citizen,print Not Eligible.
if age is below 18,print how many years are left before the user can vote.
(=,== difference)


"""


Age = int(input('Enter the Age:'))
if (Age>=18):
    Indian_citizen=input("Are you an Indian citizen(Yes/No)")
    if (Indian_citizen=="Yes"):
        voter_id=input("Do you have voter Id (Yes/No)")
        if (voter_id=="Yes"):
            print("You are eligible to vote.")
        else:
            print("Apply for voter Id")
    else:
        print("Apply for Indian_citizenship")
else:
    print(f"Age is below 18 and {18-Age} year is still left to become 18 years old")                    