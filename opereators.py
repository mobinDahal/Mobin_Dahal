# Arithemetic operators
# +,_,*,/,//,%,**
# print(2+2)
# print("ram"+"sita")
# print(100/2)
# print(23%5)
# print(23//5) # // lay pachadi ko point dedaina# .

# Assignment operators
# =,+=,-=,*=,/=
# x = 10
# x += 23
# print(x)

# Logical operators
# And, or , not


# Comparison Operator = to compare either the statemnet is true or false
# ==,<,>,>=,!=,<=


# Bitwise Operators
# &,|


# Special Operators [Its two types are as follows]
# Identity Operators: is, is not
# Merbership Operators: in, not in

# x = 4
# y = 29
# z = x
# print(x is y)
# print(x is not y)
# print(x is z)
# print(id(x))
# print(id(y))
# print(id(z))  # They are identity operators which gives the value either true or false
#
# name = 'mobin'  # membership operator
# print("x" in name)
# print("o" in name)
# print("t" in name)
#
# P = int(input("Enter P: "))
# T = int(input("Enter T: "))
# R = int(input("Enter R: "))
# print(type(R))
# m=(P * T * R) / 100
# print(m)

name = input("Enter a name: ")

print("Name is ", name)
science = int(input("Enter marks of science: "))
nepali = int(input("Enter marks of nepali: "))
social = int(input("Enter marks of social: "))
maths = int(input("Enter marks of maths: "))
english = int(input("Enter marks of english: "))
t = science + social + nepali + maths + english
print("Total marks is: ", t)
print("percentage is: ", (t / 5), "%")
