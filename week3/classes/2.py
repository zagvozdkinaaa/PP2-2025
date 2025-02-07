class Shape:
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, length):
        self.length=length

    def area(self):
        return self.length ** 2
    
shape = Shape()
print (f"Shape area: {shape.area()}")
n=int(input("Input a side of the square: "))
square = Square(n)
print (f"Square area: {square.area()}")