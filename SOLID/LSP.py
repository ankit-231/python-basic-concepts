# Liskov Substitution Principle

"""
It states that the child class should be able to replace the parent class without breaking the code, that means say a function was written for parent. If you were to replace the parameter that is the parent with
the child, the function should still work. 
"""

# Say I have a bird class

class Bird:
    def __init__(self, height) -> None:
        self.height = height

    def fly(self):
        print("I can fly")

# Penguin class extends Bird
class Penguin(Bird):
    def __init__(self, height) -> None:
        super().__init__(height)
    
    def fly(self):
        print("I cannot fly")

def make_them_fly(bird: Bird):
    bird.fly()

birdie = Bird(12)
penguini = Penguin(12)

make_them_fly(birdie)

make_them_fly(penguini)

"""
As we can see, our code, i.e, make_them_fly() funciton does not raise an error if its 
parameter is Bird obj or Penguin obj.
"""

"""
Let q(x) be a property provable about objects of x of type T. Then q(y) should be provable for objects y of type S where S is a subtype of T.

q(x) -> make_them_fly(bird)   | x is of type T: bird is of type Bird
q(y) -> make_them_fly(penguini) | y is of type S: penguini is of type Penguin


S is a subtype of T
Penguin is subtype(or subclass) of bird.
"""