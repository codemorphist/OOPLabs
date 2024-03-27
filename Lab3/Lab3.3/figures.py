from abc import ABC, abstractmethod
from typing import TypeAlias
from math import pi, sqrt


# Alias for length of sides and perimeter
Len: TypeAlias = int | float
Area: TypeAlias = int | float
Volume: TypeAlias = int | float


def validate(func): 
    """
    Decorator, which modify function to calculate 
    perimeter, area or heigth only if figure exist
    else return 0
    """
    def inner(self, *args, **kwargs):
        if not self.valid: return 0
        return func(self, *args, **kwargs)
    return inner


class Figure(ABC):
    _dimention: int # dimention of Figure

    @property
    def dimention(self) -> int:
        """
        Return dimention of figure
        """
        return self._dimention

    @abstractmethod
    def volume(self) -> Area | Volume:
        """
        Return volume of figure 
        Area - if 2D figure
        Volume - if 3D figure
        """
        pass

    @property
    @abstractmethod
    def valid(self) -> bool:
        """
        Return true if figure can exist
        """
        pass

    @property
    def name(self):
        return type(self).__name__

    def __repr__(self):
        return str(self)

    
class Figure2D(Figure):
    _dimention = 2

    @property
    @abstractmethod
    def perimeter(self) -> Len:
        """
        Return perimeter of figure
        """
        pass

    @property
    @abstractmethod
    def area(self) -> Len:
        """
        Return area of figure
        """
        pass

    def square(self) -> Area:
        return self.area

    def volume(self) -> Area:
        return self.area


class Figure3D(Figure):
    _dimention = 3

    @abstractmethod
    def volume(self) -> Area:
        """
        Return volume of figure
        """
        pass

    def square_surface(self) -> Area:
        """
        Return area of figure surface
        """
        pass

    def square_base(self) -> Area:
        """
        Return area of figure base
        """
        pass

    @property
    def heigth(self) -> Len:
        """
        Return len of figure height
        """
        pass 


class Polygon(Figure2D):
    @property
    @validate
    def perimeter(self) -> Len:
        return sum(self.sides)
        
    @property
    def valid(self) -> bool:
        """
        If Polygon have 0 size side return False
        """
        return not 0 in self.sides

    def __str__(self) -> str:
        return f"({self.name}) {self.sides}"


class Triangle(Polygon):
    def __init__(self, a: Len, b: Len, c: Len):
        self.sides: list[Len] = [a, b, c]

    @property
    @validate
    def area(self) -> Area:
        """
        Gerone formula:
        [S = sqrt(p * (p-a) * (p-b) * (p-c))]
        """
        p = self.perimeter / 2
        a, b, c = self.sides
        return sqrt(p * (p-a) * (p-b) * (p-c))

    @property
    def valid(self) -> bool:
        """
        Use Triangle rule
        """
        a, b, c = self.sides
        if a > b + c: return False
        if b > a + c: return False
        if c > a + b: return False
        return True


class Rectangle(Polygon):
    def __init__(self, a: Len, b: Len):
        self.sides: list[Len] = [a, b, a, b]

    @property
    @validate
    def area(self) -> Area:
        a, b = self.sides[0:2]
        return a * b


class Trapeze(Polygon):
    def __init__(self, base1: Len, base2: Len, 
                 side1: Len, side2: Len):
        self.sides: list[Len] = [base1, base2, 
                                 side1, side2]

    @property
    @validate
    def heigth(self) -> Len:
        """
        Calculate heigth of Trapeze.
        Split Trapeze to Triangle and Parallelogram,
        calculate area of Triangle with sides [b1-b2, s1, s2],
        after this in that Trianle use formula: 
        [S = 1/2 * a * h] to find [h]
        """
        b1, b2, s1, s2 = self.sides
        if b1 == b2:
            return s1
        tr = Triangle(s1, s2, abs(b1-b2))
        return 2 * tr.area / abs(b1 - b2)

    @property
    @validate
    def area(self) -> Area:
        """
        Use formula:
        [S = (a+b) / 2 * h]

        If sides are equal:
        [S = a * b]
        """
        a, b = self.sides[0], self.sides[1]
        if a == b: 
            return a * self.sides[2]
        return abs(a + b) * 0.5 * self.heigth

    @property
    def valid(self) -> Area:
        """
        Use Triangle rule
        """
        b1, b2, s1, s2 = self.sides
        if b1 == b2: 
            return s1 == s2  
        else:
            return b2 - b1 < s2 + s1  


class Parallelogram(Polygon):
    def __init__(self, a: Len, b: Len, heigth: Len):
        self.sides = [a, b, a, b]
        self.heigth = heigth

    @property
    @validate
    def area(self) -> Area:
        """
        Use formula:
        [S = 1/2 * a * h]
        """
        a = max(self.sides)
        return a * self.heigth * 0.5

    def __str__(self) -> str:
        return f"[{self.name}] ({self.sides[0]}, {self.sides[1]}, {self.heigth})"

        
class Circle(Figure2D):
    def __init__(self, r: Len):
        self.r = r

    @property
    @validate
    def perimeter(self) -> Len:
        """
        Use formula:
        [P = 2 * pi * r]
        """
        return 2 * pi * self.r

    @property
    @validate
    def area(self) -> Area:
        """
        Use formula:
        [S = pi * r^2]
        """
        return pi * self.r**2

    @property
    def valid(self) -> bool:
        """
        Circle always exis with any radius > 0
        If radius is 0, area and perimeter also 0
        """
        return True
        
    def __str__(self) -> str:
        return f"({self.name}) [{self.r}]"


class Ball(Figure3D):
    def __init__(self, r: Len):
        self.r = r

    @property
    def valid(self) -> bool:
        """
        Ball always can exist with any radius
        """
        return True

    @validate
    def square_surface(self) -> Area:
        return 4*pi*self.r**2

    @validate
    def volume(self) -> Volume:
        return 4/3*pi*self.r**3

    def __str__(self) -> str:
        return f"({self.name}) [{self.r}]"


class TriangularPyramid(Figure3D):
    def __init__(self, a: Len, heigth: Len):
        self.a = a  # Len of base side
        self.height = heigth   # Height of pyramid 

    @property
    def valid(self) -> bool:
        return self.a > 0 and self.height > 0
    
    @validate
    def square_base(self) -> Area:
        """
        Area of right triangle
        """
        return self.a**2*sqrt(3)/4

    @validate
    def square_surface(self) -> Area:
        """
        Calculate square of surface triangle and multiply by 3
        """
        base_mediane = self.a*sqrt(3)/2
        surf_triangle_height = sqrt( (1/3 * base_mediane)**2 + self.height**2 )
        return 3/2 * self.a * surf_triangle_height

    @validate
    def volume(self) -> Volume:
        return self.height * self.square_base() / (4 * sqrt(3))
        
    def __str__(self) -> str:
        return f"({self.name}) [{self.a}, {self.height}]"


class QuadrangularPyramid(Figure3D):
    def __init__(self, a: Len, b: Len, height: Len):
        self.a = a
        self.b = b
        self.height = height

   
    @property
    def valid(self) -> bool:
        return self.a > 0 and self.b > 0 and self.height > 0

    @validate
    def square_surface(self) -> Area:
        """
        Calculate apothems and calculate area of side triangles 
        by formule [S=1/2*a*h]
        """
        height = self.height
        a, b = self.a, self.b
        surf_a_height = sqrt(height**2 + (b/2)**2)
        surf_b_height = sqrt(height**2 + (a/2)**2)
        trngl_a_area = 1/2 * a * surf_a_height
        trngl_b_area = 1/2 * b * surf_b_height
        return 2*trngl_a_area + 2*trngl_b_area

    @validate
    def square_base(self) -> Area:
        """
        Return area of base rectangle
        """
        return self.a * self.b

    @validate 
    def volume(self) -> Volume:
        return 1/3 * self.square_base() * self.height

    def __str__(self) -> str:
        return f"({self.name}) [{self.a}, {self.b}, {self.height}]"


class RectangularParallelepiped(Figure3D):
    def __init__(self, a: Len, b: Len, c: Len):
        self.a = a
        self.b = b
        self.c = c

    @property
    def valid(self) -> bool:
        return self.a > 0 and self.b > 0 and self.c > 0

    @validate
    def square_surface(self) -> Area:
        a, b, c = self.a, self.b, self.c
        return 2*a*c + 2*b*c

    @validate
    def square_base(self) -> Area:
        return self.a * self.b

    @validate
    def volume(self) -> Volume:
        return self.a * self.b * self.c

    def __str__(self) -> str:
        return f"({self.name}) [{self.a}, {self.b}, {self.c}]"

class Cone(Figure3D):
    def __init__(self, r: Len, height: Len):
        self.r = r
        self.height = height

    @property
    def valid(self) -> bool:
        return self.r > 0 and self.height > 0

    @validate
    def square_surface(self) -> Area:
        """
        Clculate apothem and side area by formule
        [S=pi*r*L]
        """
        L = sqrt(self.r ** 2 + self.height ** 2)
        return pi * self.r * L

    @validate
    def square_base(self) -> Area:
        return Circle(self.r).area

    @validate
    def volume(self) -> Volume:
        return 1/3 * self.square_base() * self.height

    def __str__(self) -> str:
        return f"({self.name}) [{self.r}, {self.height}]"


class TriangularPrism(Figure3D):
    def __init__(self, a: Len, b: Len, c: Len, height: Len):
        self.sides = [a, b, c]
        self.height = height

    @property
    def valid(self) -> bool:
        return Triangle(*self.sides).valid and self.height > 0

    @validate 
    def square_surface(self) -> Area:
        surf_area = 0
        for s in self.sides:
            surf_area += s * self.height
        return surf_area
    
    @validate
    def square_base(self) -> Area:
        return Triangle(*self.sides).area

    @validate
    def volume(self) -> Volume:
        return self.square_base() * self.height

    def __str__(self) -> str:
        return f"({self.name}) [{self.sides}, {self.height}]"

