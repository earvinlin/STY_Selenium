import math

class Point:
    def __init__(self, x = 0, y = 0) :
        self.x = x
        self.y = y
    
    def distance_from_origin(self) :
        return math.hypot(self.x, self.y)

#   https://vimsky.com/zh-tw/examples/usage/str-vs-repr-in-python.html
#   repr() vs. str() [repr() == !r ; str() == !s]
    def __repr__(self) :
        return "Point({0.x!r}, {0.y!r})".format(self)
    
    def __str__(self) :
        return "({0.x!r}, {0.y!r})".format(self)