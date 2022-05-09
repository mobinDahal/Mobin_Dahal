################################# HOMEWORK 3 #################################

users = [
    ["user", "admin"],
    ["none1", "noone"],
    ["home", "school"],
    ["very", "good"],
    ["mobin", "dahal"]

]

input_username = input("Enter username: ")
enput_password = input("Enter password: ")
total_users = len(users)
increament = 0
login_success = False
while increament < total_users:
    uname = users[increament][0]
    upass = users[increament][1]
    if input_username == uname and enput_password == upass:
        login_success = True
    increament += 1
if login_success:
    print(f"welcome {input_username}")
else:
    print("incorrect username and password")
