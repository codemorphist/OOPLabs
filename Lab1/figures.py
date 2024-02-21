from abc import ABC, abstractmethod
from typing import TypeAlias
from math import pi, sqrt

# Alias for length of sides and perimeter
Len: TypeAlias = int | float
Area: TypeAlias = int | float

def validate(func): 
    """
    Decorator, which calculate perimeter, area or perimeter
    only if figure with parameters exist
    """
    def inner(self, *args, **kwargs):
        if not self.valid: return 0 
        return func(self, *args, **kwargs)
    return inner

class Figure(ABC):
    @property
    @abstractmethod
    def perimeter(self) -> Len:
        pass

    @property
    @abstractmethod
    def area(self) -> Len:
        pass

    @property
    @abstractmethod
    def valid(self) -> bool:
        pass

    @property
    def name(self):
        return type(self).__name__


class Polygon(Figure):
    def __init__(self):
        super().__init__()

    @property
    @validate
    def perimeter(self) -> Len:
        return sum(self.sides)
        
    @property
    def valid(self) -> bool:
        return not 0 in self.sides

    def __str__(self) -> str:
        return f"[{self.name}] ({self.sides})"


class Triangle(Polygon):
    def __init__(self, a: Len, b: Len, c: Len):
        super().__init__()
        self.sides: list[Len] = [a, b, c]

    @property
    @validate
    def area(self) -> Area:
        p = self.perimeter / 2
        a, b, c = self.sides
        return sqrt(p * (p-a) * (p-b) * (p-c))

    @property
    def valid(self) -> bool:
        a, b, c = self.sides
        if a > b + c: return False
        if b > a + c: return False
        if c > a + b: return False
        return True


class Rectangle(Polygon):
    def __init__(self, a: Len, b: Len):
        super().__init__()
        self.sides: list[Len] = [a, b, a, b]

    @property
    @validate
    def area(self) -> Area:
        a, b = self.sides[0:2]
        return a * b


class Trapeze(Polygon):
    def __init__(self, base1: Len, base2: Len, 
                 side1: Len, side2: Len):
        super().__init__()
        self.sides: list[Len] = [base1, base2, 
                                 side1, side2]

    @property
    @validate
    def heigth(self) -> Len:
        b1, b2, s1, s2 = self.sides
        if b1 == b2:
            return s1
        tr = Triangle(s1, s2, abs(b1-b2))
        return 2 * tr.area / abs(b1 - b2)

    @property
    @validate
    def area(self) -> Area:
        a, b = self.sides[0], self.sides[1]
        if a == b: 
            return a * self.sides[2]
        return abs(a + b) * 0.5 * self.heigth

    @property
    def valid(self) -> Area:
        b1, b2, s1, s2 = self.sides
        if b1 == b2: 
            return s1 == s2  
        else:
            return b2 - b1 < s2 + s1  


class Parallelogram(Polygon):
    def __init__(self, a: Len, b: Len, heigth: Len):
        super().__init__()
        
        self.sides = [a, b, a, b]
        self.heigth = heigth

    @property
    @validate
    def area(self) -> Area:
        a = max(self.sides)
        return a * self.heigth * 0.5

        
class Circle(Figure):
    def __init__(self, r: Len):
        super().__init__()
        self.r = r

    @property
    @validate
    def perimeter(self) -> Len:
        return 2 * pi * self.r

    @property
    @validate
    def area(self) -> Area:
        return pi * self.r**2

    @property
    def valid(self) -> bool:
        return True
    
    def __str__(self) -> str:
        return f"[{self.name}] ({self.r})"

