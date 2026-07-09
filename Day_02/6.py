"""Take input:

Age
Monthly Salary
Credit Score
Existing Loan (yes/no)

Rules:

Age must be at least 21.
If salary is at least ₹50,000:
If credit score is at least 750:
If there is no existing loan → Loan Approved
Otherwise → Loan Rejected: Existing Loan
Otherwise → Low Credit Score
Otherwise → Insufficient Salary
If age is below 21 → Not Eligible"""

age = int(input("enter your age:"))
monthly_salary = int(input("enter your monthly salary"))
credit_score = int(input("enter your credit score"))
existing_loan = input("does you have existing loan:(yes/no)").lower()

if (age >= 21):
    if (monthly_salary >= 50000):
        if (credit_score >= 750):
            if (existing_loan == "no"):
                print("Loan approved")
            else:
                print("Loan rejected: existing loan")
        else:
            print("Loan rejected: low credit score")
    else:
        print("Loan rejected: Insufficient salary")
else:
    print("Loan rejected: not eligible")                            
           