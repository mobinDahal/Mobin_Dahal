# Conditon Statement (control statement)
# if
# elif
# else
# nested if else

# x=10
# y=20
# if x>y:
#     print(" x is large ")
# else:
#     print(" y is large")

# x=10
# y=20
# z=30
# if x>y and x>z:
#     print("x is greater")
# elif y>x and y>z:
#     print("y is large")
# else:
#     print("z is large")

# Question 1
# username = input("Enter username " )
# Enter_password = input("Enter password ")
# given_username = "ram"
# gien_password = "ram002"
# if username == given_username and Enter_password== gien_password or username=="admin" and Enter_password=="admin002":
#     print("Welcome to the program")
# else:
#     print("your username and password is wrong")


# Question 2
# Enter_age = int(input("Enter your age "))
# if Enter_age<18:
#     print("you are not eligible to the party because you are a child")
# elif Enter_age>=18 and Enter_age<=40:
#     print("welcome to the party")
# else:
#     print("you are a not eligible")

# Question 3
name = input("Enter a name: ")

print("Name is ", name)
science = int(input("Enter marks of science: "))
# if science>100:
#     print("exit")
#     exit()
nepali = int(input("Enter marks of nepali: "))
social = int(input("Enter marks of social: "))
maths = int(input("Enter marks of maths: "))
english = int(input("Enter marks of english: "))


# if science < 0 and science > 100 or social < 0 and social > 100 or nepali < 0 and nepali > 100 or english < 0 and english > 100 or maths < 0 and maths > 100:
#     print("The value you have entered is wrong")

t = science + social + nepali + maths + english
print("Total marks is: ", t)
a = t / 5
print("percentage is: ", a, "%")
if a < 35:
    print("you are fail")
elif a >= 35 and a < 45:
    print("You got third division")
elif a >= 45 and a < 60:
    print("You got second division")
elif a >= 60 and a < 75:
    print("You got first division")
elif a >= 75 and a <= 100:
    print("Wow, congralutation you got distinction")


# Computer Bazar
# 1. dell(18000) 2. toshiva(30000) 3.mac(30000)
#select options:1
#quantity ?
 # delivary options
 # 1 hancha vane home 2 hancha vane pickup
 #packing
 # 1 hancha vane plastic 2 hancha vane bag 3 gift pack
 # lobcation
 #ktm(13