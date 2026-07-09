"""Create a list containing the correct answers:
":zx 
["A", "C", "B", "D", "A"]

Take 5 answers from the user.

Without using loops:

Count the number of correct answers.
Print:
Total correct answers
Total wrong answers
Percentage
If percentage ≥ 80 → Pass with Distinction
50-79 → Pass
Otherwise → Fail"""


correct_answer = ["A","C","B","D","A"]
answer_from_user = input("tell all the answer for all question and seprate them by coma")
user_answer = answer_from_user.split(",")
official_correct = 0

if (user_answer[0] == correct_answer[0]):
    official_correct += 1
if (user_answer[1] == correct_answer[1]):
        official_correct += 1
if(user_answer[2] == correct_answer[2]):
            official_correct += 1
if (user_answer[3] == correct_answer[3]):
                official_correct += 1
if (user_answer[4] == correct_answer[4]):
                    official_correct += 1
                   
                    
                
wrong_answer = 5 - official_correct
print(wrong_answer)
print(official_correct)


percentage = (official_correct/5)*100

if (percentage >= 80):
    print("pass with distinction")
elif (50 <= percentage < 79):
    print("pass")
else:
    print("fail")        


    





 