# declare a class
# class introduction:
    # body part of the class
    # x = 10 # it is an attribute
    # def test(self):  # it is the behaviour
    #     pass
# eclare an objet instane of the class
# obj =  introduction()
# access the object
# print(obj.x)
# print(obj.test())



# class students:
#     def name(self,name):
#         print(f'student name is {name}')
#
#     def age(self,age):
#         print(f'Student age is {age}')
#
# obj = students()
# obj.name("Mobin")
# obj.age(17)
# obj.name("samir")
# obj.age(19)



class user:
    name = "mobin"

    def get_name(self):
        print(self.name)
        print(self.age)

    def age(self):
        return 10

obj = user()
obj.get_name()
obj.age()