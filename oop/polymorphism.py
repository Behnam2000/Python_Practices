from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass
    
class Circle(Shape):

    def __init__(self, redius):
        self.radius = redius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Pizza(Circle):
    def __init__(self, topping, redius):
        super().__init__(redius)
        self.topping = topping


shapes = [Circle(4), Square(6), Pizza("pepperoni", 13)]

for shape in shapes:
    print(f"{shape.area()}cm2")