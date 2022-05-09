################### CLASSWORK ###################

# x =10
# while x>0:
#     print(x,end=" ")
#     x-=1

# stop iteration: break, continue
# x = 0
# while x < 10:
#     x += 1
#     if x == 1 or x == 4 or x == 9:
#         continue
#     else:
#
#         print(x, end=" ")


num = int(input("Enter number of students: "))
increment =1
students_name=[]
while increment<=num:
    name = input("Enter name: ")
    students_name.append(name)
    increment+=1

