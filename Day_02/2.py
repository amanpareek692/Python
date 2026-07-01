"""create a list of 5 student marks.
Ask the user to enter a subject number(1-5)
if the subject number is valid,display the ocreesponding marks.
if the marks are above 90,print excellent
if the marks are between 75 and 89,print good
otherwise,print Needs Improvement.
if the subject number is invalid,print invalid subject number"""


Student_marks = [87,98,32,45,65]
Subject_number = int(input("Enter the Subject_number:"))


if (Subject_number==1):
    print(Student_marks[0])
    if(Student_marks[0] >= 90):
        print("Excellent")
    elif(89>= Student_marks >= 75):
        print("Good")
    else:
        print("Needs Improvement")
elif(Subject_number==2):
    print(Student_marks[1])
    if(Student_marks[1] >= 90):
        print("Excellent")
    elif(89>= Student_marks[1] >= 75):
        print("Good")
    else:
        print("Needs Improvement")
elif(Subject_number==3):
    print(Student_marks[2])
    if(Student_marks[2]>= 90):
        print("Excellent")
    elif(89>= Student_marks[2] >= 75):
        print("Good")
    else:
        print("Needs Improvement")
elif(Subject_number==4):
    print(Student_marks[3]) 
    if(Student_marks[3] >= 90):
        print("Excellent")
    elif(89>= Student_marks[3] >= 75):
        print("Good")
    else:
        print("Needs Improvement")       
elif(Subject_number==5):
    print(Student_marks[4]) 
    if(Student_marks[4] >= 90):
        print("Excellent")
    elif(89>= Student_marks[4] >= 75):
        print("Good")
    else:
        print("Needs Improvement")   
else:
    print("The Subject code is invalid")




