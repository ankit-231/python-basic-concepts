import math

class Square:
    def __init__(self, length) -> None:
        self.length = length

class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius

class AreaCalculator:
    def __init__(self, shapes: list) -> None:
        self.shapes = shapes

    def sum_(self) -> float:
        area = []
        for shape in self.shapes:
            if isinstance(shape, Square):
                area.append(shape.length**2)
            
            elif isinstance(shape, Circle):
                area.append(math.pi * ((shape.radius)** 2))

        return sum(area)
    
    # def output(self) -> str:

    #     return ("the sum is", self.sum_())
    
shapes = [Circle(2), Square(5), Square(6)]

areas = AreaCalculator(shapes)


# here AreaCalculator class deals with getting the sum of shapes and output of shapes. if we wanted to
# get output in different format like json or html, we'd have to do it in AreaCalculator class.
# output should be handled by different class so as to not violate SRP. Single-Responsibility Principle


class SumCalculatorOutputter:
    def __init__(self, calculator: AreaCalculator) -> None:
        self.calculator = calculator

    def JSON(self):
        data = self.calculator.sum_()
        

        return {"json":  data}
    
    def HTML(self):
        data = "HTML DATA " + str(self.calculator.sum_())

        return data
    
shapes = [ Circle(2), Square(5), Square(6) ]

areas = AreaCalculator(shapes)

output = SumCalculatorOutputter(areas)

print(output.HTML())
print(output.JSON())

# this follows SRP
      


