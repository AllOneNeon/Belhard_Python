from abc import ABC, abstractmethod

class Shape (ABC):
    def __init__ (self, area, perimeter):
        self.area = area
        self.perimeter = perimeter

    @property
    @abstractmethod
    def s (self):
        pass

class Point:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__ (self, start: Point, end: Point):
        self.start = start
        self.end = end

    def length_get (self):
        x1 = self.start.x
        x2 = self.end.x
        y1 = self.start.y
        y2 = self.end.y
        return ((x2 - x1)**2) + ((y2 - y1)**2)**0.5

    @property
    def length (self):
        return self.length_get ()


class Rect (Shape):
    def __init__ (self, side_a: Line, side_b: Line):
        self.side_a = side_a
        self.side_b = side_b
        self.area = side_a * side_b
        self.perimeter = side_a * 2 + side_b * 2

    @property
    def s (self):
        print (f'The area of the rectangle is {self.area} and the perimeter is {self.perimeter}')

class Square (Shape, Line):
    def __init__(self):
        self.area = side_a * side_b
        self.perimeter = side_a ** 2 + side_b ** 2
        
    @property 
    def s (self):
        print (f'The area of the square is {self.area} and the perimeter is {self.perimeter}')

class Cube (Square):
    def __init__ (self, volume):
        self.volume = volume     
        volume = side_a ** 3
        print ('The volume of the cube: ', volume)



origin = Point (0,0)
somePoint = Point (1,1)
line = Line (origin, somePoint)
print ('The length of the line: ' , line.length)
side_a = line.length
side_b = line.length
obj = Rect (side_a, side_b)
obj.s
obj1 = Square ()
obj1.s
volume = line.length ** 3
obj2 = Cube (volume)
obj2.__init__