# try:
#     print(10 / 0)
# except TypeError:
#     print("Nice")
# except ZeroDivisionError:
#     print("It is not devisible")
#
# finally:
#     print("Get lost")

def add(x,y):
    if y == 0:
        raise Exception("y cannot be zero")
    return x+y

try:
    print(add(89,27))
except Exception as e:
    print("Exception:",e)