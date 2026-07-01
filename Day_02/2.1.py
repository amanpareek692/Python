student_marks=[23,45,34,55,43]
subject_name=int(input("enter the subject_number(1-5):"))
if(1 <= subject_name <= 5):
    marks = student_marks[subject_name - 1]
    print(marks)
else:
    print('subject code is invalid')    

