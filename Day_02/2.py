


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




