print("####################Welcome to computer bazar####################")
print("We have a offer on the occasion of New Year and the most famous ones are\n"
      "1.Dell = Rs.20000\n"
      "2.Toshiba = Rs.30000\n"
      "3.Mac = Rs.50000")
dell_price = 0
toshiba_price = 0
mac_price = 0
del_price = 0
# del_pickup = 0
pac_plastic = 0
pac_bag = 0
pac_giftBox = 0
loc_ktm = 0
loc_bkt = 0
loc_ltp = 0

choice1 = int(input("choose options: "))
quantity = int(input("Enter how many of these laptops do you want: "))
if choice1 == 1:
    dell_price += 20000 * quantity
elif choice1 == 2:
    toshiba_price += 30000 * quantity
elif choice1 == 3:
    mac_price += 50000 * quantity
else:
    print("The value you have choosen is incorrect")
    exit()
print("Choose a medium to deliver\n 1. Home = Rs.1000\n 2. Pickup = Free")
choice2 = int(input("choose options: "))
if choice2 == 1:
    del_price += 1000
elif choice2 == 2:
    del_price
else:
    print("The value you have choosen is incorrect")
    exit()

print("Choose a medium to Packing\n 1. Plastic = Rs.500\n 2.  Bag = 1000\n 3. Gift Box = 5000\n 4. None")
choice3 = int(input("choose options: "))
if choice3 == 1:
    pac_plastic += 500
elif choice3 == 2:
    pac_bag += 1000
elif choice3 == 3:
    pac_giftBox += 5000
elif choice3 == 4:
    pass
else:
    print("The value you have choosen is incorrect")
    exit()

print(
    "Please select a location where it is needed to be delivered\n 1. Kathmandu(ktm)=13% tax\n 2. Bhaktpur(bkt)=free\n 3. Lalitpur(ltp)=free")
choice4 = int(input("choose options: "))
if choice4 == 1:
    if choice1 == 1:
        loc_ktm += 0.13 * dell_price
    elif choice1 == 2:
        loc_ktm += 0.13 * toshiba_price
    elif choice1 == 3:
        loc_ktm += 0.13 * mac_price
elif choice4 == 2 or choice4 == 3:
    loc_bkt
    loc_ltp

grand_total = dell_price + toshiba_price + mac_price + del_price + pac_plastic + pac_bag + pac_giftBox + loc_ktm + loc_bkt + loc_ltp
taxable_amount = loc_ktm + loc_bkt + loc_ltp
print(f"you have ordered {quantity} laptops.The grand total amount is Rs.{grand_total} and the taxable amount is Rs.{taxable_amount}")

