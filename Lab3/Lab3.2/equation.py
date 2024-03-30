from math import sqrt


REAL = ["REAL"] # constant to all REAL solutions


class Equation:
    def __init__(self, b, c):
        self._b = b
        self._c = c

    def solve(self):
        b, c = self._b, self._c

        if b == 0 and c == 0:
            return REAL
        elif b == 0:
            return []
        else:
            return [-c/b]

    def __repr__(self):
        return str(self)

    def __str__(self):
        b, c = self._b, self._c
        return f"{b}x{'+' if c >= 0 else ''}{c}"


class QuadraticEquation(Equation):
    def __init__(self, a, b, c):
        self._a = a
        super().__init__(b, c)

    @property
    def D(self) -> float | int: # discriminant
        """
        :return discriminant of quadric equation 
        """
        a, b, c = self._a, self._b, self._c
        return b**2 - 4*a*c

    def solve(self):
        D = self.D
        a, b, c = self._a, self._b, self._c

        if a == 0 and b == 0 and c == 0:
            return REAL
        if a == 0:
            return super().solve()
        elif D < 0:
            return []
        elif D == 0:
            return [-b/(2*a)]
        else:
            return [(-b + sqrt(D))/(2*a), 
                    (-b - sqrt(D))/(2*a)]

    def __str__(self):
        a = self._a
        return f"{a}x^2{'+' if self._b >= 0 else ''}{super().__str__()}"


class BiQuadraticEquation(QuadraticEquation):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def solve(self):
        sol = super().solve()
        if sol == REAL:
            return REAL
        sol = list(filter(lambda x: x >= 0, sol))
        solutions = set()
        for x in sol:
            solutions.add(sqrt(x))
            solutions.add(-sqrt(x))
        return list(solutions)

    def __str__(self):
        a, b, c = self._a, self._b, self._c
        return f"{a}x^4{'+' if b >= 0 else ''}{b}x^2{'+' if c >= 0 else ''}{c}"
