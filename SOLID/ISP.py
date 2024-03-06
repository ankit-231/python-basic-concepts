# Interface Segregation Principle

"""
This principle states that a class should not have to implement interfaces it doesnot require.
It should not be forced to have methods it does not need.

"""


# EG: I have an abstract WritingTool class

# from abc import ABC, abstractmethod, ABCMeta

# # use ABC instead of WritingTool(metaclass=ABCMeta), ABC inherits from ABCMeta. 
# # Uding just ABC is the standard

# class WritingTool(ABC):

#     @abstractmethod
#     def write(self):
#         pass

#     @abstractmethod
#     def refill(self):
#         pass

#     @abstractmethod
#     def sharpen(self):
#         pass


# class Pencil(WritingTool):

#     def write(self):
#         print("i am sketching")

#     def refill(self):
#         # nothing cause cant refill
#         pass

#     def sharpen(self):
#         print("i'm getting pointier")
    
# class Pen(WritingTool):

#     def write(self):
#         print("i am inking")

#     def refill(self):
#         print("i am refilling")


#     def sharpen(self):
#         # nothing cause cant sharpen
#         pass

"""
Here Pen and Pencil both have to implement methods they dont need. Better way to rewrite this as:
"""


from abc import ABC, abstractmethod, ABCMeta

# use ABC instead of WritingTool(metaclass=ABCMeta), ABC inherits from ABCMeta. 
# Uding just ABC is the standard

class WritingTool(ABC):

    @abstractmethod
    def write(self):
        pass


class Refilling(ABC):

    @abstractmethod
    def refill(self):
        pass

class Sharpening(ABC):

    @abstractmethod
    def sharpen(self):
        pass

class Pencil(WritingTool, Sharpening):

    def write(self):
        print("i am sketching")

    def sharpen(self):
        print("i'm getting pointier")
    
class Pen(WritingTool, Refilling):

    def write(self):
        print("i am inking")

    def refill(self):
        print("i am refilling")
