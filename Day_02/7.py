"""Create a list of 5 player scores.

Ask the user for a player number (1-5).

Rules:

If the player number is invalid → Print Invalid Player.
Otherwise:
Score ≥ 100 → Century Hero
50-99 → Half Century
30-49 → Good Performance
Below 30 → Dropped from Team"""


score = [23,45,57,87,199]
number = int(input("enter the player number from(1-5)")) 
player_score = score[number-1]


if (player_score >= 100):
    print("century her0")
elif (50 <= player_score <=99):
    print("half century")
elif (30<= player_score <=49):
    print("good performance")
else:
    print("Dropped from the team")            
