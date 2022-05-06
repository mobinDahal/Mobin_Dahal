# x=10
# y=20
# z=30
# # example nested if else statement
#
# if x>y:
#     if x>z:
#         print("x is greater than y and z")
#     else:
#         print("z si grreater than x and y")
# else:
#     if y>z:
#         print("y is greater than z")
#     else:
#         print("z is greater than y")

#@@@@@@@@@@@@@@@@@@@@@ CLASSWORD @@@@@@@@@@@@@@@@@@@@@#
username = "admin"
password = "12345"
if username == "admin":
    if password == "12345":
        print("you are logged in")

    else:
        print("Incorrect password")

else:
    if password=="12345":
        if username=="admin":
            print("you are logged in")
        else:
            print("incorrect username")
    else:
        print("incorrect username and password")
