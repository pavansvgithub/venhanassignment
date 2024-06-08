class Rectangle:
    def __init__(self,length,width):
        self.length = length 
        self.width = width 
    def area(self):
        return self.length * self.width 
    def perimeter(self):
        return 2 * (self.length + self.width)

rectangle = Rectangle(5.0,3.0)
print(rectangle.area())
print(rectangle.perimeter())