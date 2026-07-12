"""Take a 3-digit number.

Find:

Sum of digits.
Reverse of the number.
Difference between original and reverse.
Product of digits.

Finally print:

Original Number : ___
Reversed Number : ___
Digit Sum : ___
Digit Product : ___
Difference : ___"""


number = (input("enter the 3 digit number:"))

digit_sum = int(number[0]) + int(number[1]) + int(number[2])
reversed_number = int(number[::-1])
difference = int(number) - reversed_number
product_digit = int(number[0])*int(number[1])*int(number[2])

print(f"original number:{number}\nreversed number:{reversed_number}\ndigit number:{digit_sum}\ndigit product {product_digit}\ndifference:{difference}")