# i=1
# classwork1
# name =input("Enter name: ")
# times = int(input("Enter how many times you want to print: "))
# def repeat(name,time1):
#     incre =1
#     while incre<=time1:
#         print(name)
#         incre+=1
#
#
# repeat(name,times)

# classwork2
num1=int(input("enter first number:"))
num2 = int(input("enter second number: "))
def all(num1,num2):
    add= num1+num2
    sub = num1-num2
    multiply = num1*num2
    division= num1/num2
    return add,sub,multiply,division
print(all(num1,num2))
