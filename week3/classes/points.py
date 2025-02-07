import math

class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def show(self):
        print (f"({self.x},{self.y})")
    
    def move(self, newX, newY):
        self.x=newX
        self.y=newY

    def dist(self, second_point):
        return math.sqrt((second_point.x-self.x) ** 2 + (second_point.y-self.y) ** 2)

x1=int(input("Enter x1: "))
y1=int(input("Enter y1: "))
print("The first point: ")
point1=Point(x1,y1)
point1.show()

x2=int(input("Enter x2: "))
y2=int(input("Enter y2: "))
print("The second point: ")
point2=Point(x2,y2)
point2.show()
print(f"Distance between two points: {point1.dist(point2)}")

