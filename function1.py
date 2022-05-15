# Types of function
# 1. Inbuilt function
# 2. User diefined function

# Inbuilt function example:
# 1. abs()
# 2. pow()
# 3. max()
# 4. min()
# 5. round()

# print(dir(__builtins__))
# define function
# def my_function():
#     # function body
#     print("Hello World")
#
#
# # call function
# my_function()
# my_function()

# parameters examples:
# def my_function(name, age):
#     print("Hello",name,age)
# my_function("mobin",17)

# def add(x, y):
#     print(x + y)
#
#
# add(29, 32)
# add(13, 7)

# optional parameters example:

# def add(x,z,y=10):
#     print(x+y+z)
# #optonal parameter should always be kept at last
#
# add(23,2)
# add(155,5)

# def users(*name,**data):
#     print(name)
#     print(data)
#
# users("mobin","gafadi","samir","ram", name="john", age =67,address= "New York")
# def test():
#     print("hello")
# def get():
#     test()
#
# get()

# return types function

# def add(x, y):
#     return x + y
#
#
# print(add(23, 2))

# def add_sub(x,y):
#     tot = x+y
#     sub = x-y
#     return [tot, sub]
# print(add_sub(32,12))

# x=23
# def test():
#     global x
#     x+=2
#     print(x)
# test()
# print(x)

#lambda function (annyonomus function)
# a = lambda x,y:x+y
# print(a(20,30))

# factioral of 5
# n=int(input("enter a number "))
# def fac(n):
#      if n==1:
#          return 1
#      else:
#          return n* fac(n-1)
# print(fac(n))

#nested function

def pac():
    def test():
        print("hello")

    return test()

a = pac()
print(a())



