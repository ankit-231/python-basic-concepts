# OCP START
# lets assume a class Footballer

# class Footballer:
#     def __init__(self, name, age, role) -> None:
#         self.name = name
#         self.age = age
#         self.role = role

#     def getFootballerRole(self):
#         name = self.name
#         role = self.role
#         if role == "goalkeeper":
#             return name + " is " + "goalkeeper"
        
#         elif role == "defender":
#             return name + " is " + "defender"
        
#         elif role == "midfielder":
#             return name + " is " + "midfielder"

#         else:
#             return "invalid role"
        

# sam = Footballer("Sam", 19, "goalkeeper")

# print(sam.getFootballerRole())

# if i wanted to add another role like winger, i'd have to edit the getFootballerRole() function's
# if...elif...else block to add more elif. This would violate OCP. Our class is open to extension,
# for right now, for extension, we'd have to modify our code as well, hence violation of OCP.

# To solve that we create a Role parent abstract class with getRole() function and its subclasses that
# represent different roles and each have getRole() function

# so now role in Footballer would actually be an instance of Role class ko subclasses

from abc import ABC, abstractmethod

class Role(ABC):

    @abstractmethod
    def getRole(self):
        pass

    
class GoalKeeper(Role):
    
    def getRole():
        return "goalkeeper"
    
class Defender(Role):
    
    def getRole():
        return "defender"
    
class MidFielder(Role):
    
    def getRole():
        return "midfielder"

class Winger(Role):
    
    def getRole():
        return "winger"


class Footballer:
    def __init__(self, name, age, role) -> None:
        self.name = name
        self.age = age
        self.role = role
    
    def getFootballerRole(self):

        return self.name + " is " + self.role.getRole()
    

sam = Footballer("Sam", 19, GoalKeeper)

# now to add new roles, we gotta add new subclasses of Role and dont need to change
# the Footballer class itself, or the Role class

print(sam.getFootballerRole())