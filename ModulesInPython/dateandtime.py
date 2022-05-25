# from datetime import date
#
# # date object of today's date
# today = date.today()
#
# print("Current year:", today.year)
# print("Current month:", today.month)
# print("Current day:", today.day)

from datetime import datetime

# Getting Datetime from timestamp
# date_time = datetime.fromtimestamp(1653413024.174224)
# print("Datetime from timestamp:", date_time)

# from datetime import datetime
# #
today = datetime.now()

print("Current date and time is", today.timestamp())


# Creating Time object
# today = time.today()
# Time = time(12, 24, 36, 1212)
#
# # Converting Time object to string
# Str = Time.isoformat()
# print("String Representation:", Str)
# print(type(Str))