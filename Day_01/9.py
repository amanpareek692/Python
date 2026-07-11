"""A person's current monthly salary is given.

Assume:

Every year salary increases by 12%.
Find the salary after 3 years.
Also calculate the total extra money earned per month after 3 years compared to now.

Print everything using f-strings and round values to 2 decimal places.
"""


person_salary = int(input("enter the salary of the person:"))

promotion_1 = (person_salary*.12) + person_salary
promotion_2 = (promotion_1*.12) + promotion_1
promotion_3 = (promotion_2*.12) + promotion_2
extra_salary_month = (promotion_3 - person_salary)/12
extra_salary_month = round(extra_salary_month,2)

print(f"current person salary:{person_salary}\nsalary after 3 year:{promotion_3}\nextra salary earned per month by 3 year:{extra_salary_month}")