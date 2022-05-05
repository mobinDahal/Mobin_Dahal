print("@@@@@@@####### Welcome to Shaja Yatayat #######@@@@@@@")
print(
    "currently you are at kalanki.\nthe total distance covered by the bus around the ring road is 27km.\nplease select the location you want to go for.\n1. syambhu(3km)\n2. basundhara(6km)\n3. dhumbarahi(10km)\n4. chabahel(13km)\n5. koteshor(21km)\n6. satdobato(25km)\n7. for a full ring road ride(27km)")

choice1 = int(input("Enter number indicated by places: "))


# total_distance = 27
bus_fair = 0
price_for_4km = 15
unit_price = 15 / 4
if choice1 == 1:
    bus_fair += unit_price * 3
elif choice1 == 2:
    bus_fair += unit_price * 6
elif choice1 == 3:
    bus_fair += unit_price * 10
elif choice1 == 4:
    bus_fair += unit_price * 13
elif choice1 == 5:
    bus_fair += unit_price * 21
elif choice1 == 6:
    bus_fair += unit_price * 25
elif choice1 == 7:
    bus_fair += unit_price * 27
else:
    print("The value you have choosen is incorrect")
    exit()
choice2 = input("Enter y if you have a student card or old aged card else enter n: ")
if choice2=="y":
    bus_fair-= bus_fair * 0.1
elif choice2=="n":
    bus_fair
else:
    print("The value you have choosen is incorrect")
    exit()
print(f"The total amount of your journey is {bus_fair}")