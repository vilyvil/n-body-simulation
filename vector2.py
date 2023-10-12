import math

class Vector2:
    x = 0
    y = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(a, b):
        if (type(b) == Vector2):
            return(Vector2(a.x + b.x, a.y + b.y))
        return Vector2(a.x + b, a.y + b)

    def __sub__(a, b):
        if (type(b) == Vector2):
            return(Vector2(a.x - b.x, a.y - b.y))
        return Vector2(a.x - b, a.y - b)

    def __mul__(a, b):
        if (type(b) == Vector2):
            return(Vector2(a.x * b.x, a.y * b.y))
        return Vector2(a.x * b, a.y * b)
    
    def __truediv__(a, b):
        if type(b) == Vector2:
            return Vector2(a.x / b.x, a.y / b.y)
        return Vector2(a.x / b, a.y / b)

def GetMagnitude(vector):
    return math.sqrt(pow(vector.x, 2) + pow(vector.y, 2))

def Normalize(vector):
    mag = GetMagnitude(vector)
    if mag == 0:
        return vector

    return Vector2(vector.x / mag, vector.y / mag)

def SetMagnitude(vector, num):
    return Normalize(vector) * num