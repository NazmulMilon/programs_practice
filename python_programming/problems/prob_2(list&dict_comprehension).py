# Write a python program to make the data given below using list and dictionary comprehension and print it.								10
#
# data={1:[2,3,4,5],2:[1,3,4,5],3:[1,2,4,5],4:[1,2,3,5],5:[1,2,3,4]}
lst = []
square_dict = {}
# for num in range(1, 6):
for i in range(1, 6):
    lst.append(i)
    square_dict[i] = lst
print(square_dict)

cnt = 1
for i in square_dict:
    print(i, square_dict[i])
