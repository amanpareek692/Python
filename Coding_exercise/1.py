"""in this question you have to make a matrix in whic you can take the 
postion and mark the location int the matrix"""



list1 = [11,12,13]
list2 = [21,22,23]
list3 = [31,32,33]

final_matrix = [list1,list2,list3]

print(f"{list1}\n{list2}\n{list3}")

position = input("enter the position into two digit word:")

position1 = (int(position[0])-1)
position2 = (int(position[1])-1) 
row_selected = (final_matrix[position1])
column_selected = row_selected[position2] = 'x'


print(f"{list1}\n{list2}\n{list3}")


