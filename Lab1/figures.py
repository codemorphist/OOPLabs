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


class Polygon(Figure):
    @property
    def perimeter(self) -> Len:
        return sum(self.sides)


class Triangle(Polygon):
    def __init__(self, a: Len, b: Len, c: Len):
        self.sides: list[Len] = [a, b, c]

    @property
    def area(self) -> Area:
        p = self.perimeter / 2
        a, b, c = self.sides
        return sqrt(p * (p-a) * (p-b) * (p-c))


class Rectangle(Polygon):
    def __init__(self, a: Len, b: Len):
        self.sides: list[Len] = [a, b, a, b]

    @property
    def area(self) -> Area:
        a, b = self.sides
        return a * b


class Trapeze(Polygon):
    def __init__(self, base1: Len, base2: Len, 
                 left_side: Len, right_side: Len):
        if base2 < base1:
            base2, base1 = base1, base2
        self.sides: list[Len] = [base1, base2, 
                                 left_side, right_side]

    @property
    def heigth(self) -> Len:
        b1, b2, ls, rs = self.sides
        db = b2 - b1
        x = (ls**2 - rs**2 + db**2) / (2*db)
        return sqrt(ls**2 - x**2)

    @property
    def area(self) -> Area:
        a, b = self.sides[0], self.sides[1]
        return (a + b) / 2 * self.heigth


class Parallelogram(Polygon):
    def __init__(self, a: Len, b: Len, heigth: Len):
        self.sides = [a, b, a, b]
        self.heigth = heigth

    @property
    def area(self) -> Area:
        a = self.sides
        return a * self.heigth * 0.5

        
class Circle(Figure):
    def __init__(self, r: Len):
        self.r = r

    @property
    def perimeter(self) -> Len:
        return 2 * pi * self.r

    @property
    def area(self) -> Area:
        return pi * r**2
