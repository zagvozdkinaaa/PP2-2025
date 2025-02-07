class Shape:
    def area(self):
        return 0
class Rectangle:
    def __init__(self, length, width):
        self.length=length
        self.width=width

    def area(self):
        return self.length * self.width
    
shape = Shape()
print (f"Shape area: {shape.area()}")
n=int(input("Input the length of the rectangle: "))
m=int(input("Input the width of the rectangle: "))
rectangle = Rectangle(n,m)
print (f"Square area: {rectangle.area()}")