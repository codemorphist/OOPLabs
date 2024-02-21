from abc import ABC, abstractmethod
from typing import TypeAlias
from math import pi, sqrt

# Alias for length of sides and perimeter
Len: TypeAlias = int | float
Area: TypeAlias = int | float


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


class Polygon(Figure):
    @property
    def perimeter(self) -> Len:
        return sum(self.sides)

    @property
    def get_perimeter(self) -> Len:
        if not self.valid: 
            return 0
        return self.perimeter
        
    @property
    def valid(self) -> bool:
        return not 0 in self.sides

    @property
    def get_area(self) -> Area:
        if not self.valid:
            return 0
        else:
            return self.area


class Triangle(Polygon):
    def __init__(self, a: Len, b: Len, c: Len):
        self.sides: list[Len] = [a, b, c]

    @property
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
        self.sides: list[Len] = [a, b, a, b]

    @property
    def area(self) -> Area:
        a, b = self.sides[0:2]
        return a * b


class Trapeze(Polygon):
    def __init__(self, base1: Len, base2: Len, 
                 side1: Len, side2: Len):
        if base2 < base1:
            base2, base1 = base1, base2
        if side1 < side2:
            side1, side2 = side2, side1
        self.sides: list[Len] = [base1, base2, 
                                 side1, side2]

    @property
    def heigth(self) -> Len:
        b1, b2, ls, rs = self.sides
        print(self.sides)
        db = b2 - b1
        x = (ls**2 - rs**2 + db**2) / (2*db)
        return sqrt(ls**2 - x**2)

    @property
    def area(self) -> Area:
        a, b = self.sides[0], self.sides[1]
        return (a + b) / 2 * self.heigth

    @property
    def valid(self) -> Area:
        b1, b2, ls, rs = self.sides
        if b2 >= ls + b1 + rs:
            return False
        return True


class Parallelogram(Polygon):
    def __init__(self, a: Len, b: Len, heigth: Len):
        if a < b: a, b = b, a

        self.sides = [a, b, a, b]
        self.heigth = heigth

    @property
    def area(self) -> Area:
        a = self.sides[0]
        return a * self.heigth * 0.5

        
class Circle(Figure):
    def __init__(self, r: Len):
        self.r = r

    @property
    def get_perimeter(self) -> Len:
        return self.perimeter

    @property
    def get_area(self) -> Len:
        return self.area

    @property
    def perimeter(self) -> Len:
        return 2 * pi * self.r

    @property
    def area(self) -> Area:
        return pi * self.r**2

    @property
    def valid(self) -> bool:
        return True
