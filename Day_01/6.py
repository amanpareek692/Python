"""take-length and width of rectangle
calculate-area,perimeter and diagonal
round the diagonal to 2 decimal place and
print all usinf f string"""




length = int(input("enter the length:"))
width = int(input("enter the width"))
area = (width*length)
perimeter = 2*(length + width)
diagonal = (length**2 + width**2)**0.5
diagonal_round = round(diagonal,2)
print(f"are is {area} , perimeter is {perimeter} and the diagonal of rectangle is {diagonal_round}")
