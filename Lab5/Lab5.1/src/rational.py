from math import gcd


class Rational:
    def __new__(cls, *args):
        if len(args) > 2:
            raise Exception(f"Too many arguments for Rational number")

        self = super().__new__(cls)
        if isinstance(args[0], str):
            cls.__from_string__(self, args[0])
            return self

        for val in args:
            if not isinstance(val, int):
                raise Exception(f"Not valid type parameter ({val}) for Rational number")

        cls.__from_nums__(self, *args)
        return self
            
    def __from_string__(self, rstr: str) -> None:
        if rstr.count("/") > 1:
            raise Exception(f"Not valid string of Rational number: {rstr}")
        
        n, d = None, None
        if "/" in rstr:
            a, b = rstr.split("/")
            n = int(a)
            d = int(b)
        else:
            n = int(rstr)
            d = 1

        self.__from_nums__(n, d)
        
    def __from_nums__(self, n: int, d: int=1) -> None:
        if d == 0:
            raise Exception("Zero division in Rational number")
        if d < 0:
            d = abs(d)
            n = -n

        self._n = n
        self._d = d

        self.__simplify__()

    def __repr__(self) -> str:
        return f"Rational{self._n, self._d}"

    def __simplify__(self) -> None:
        n, d = self
        if n == 0:
            return
        g = gcd(n, d)
        self._n = n // g
        self._d = d // g

    def __str__(self) -> str:
        return f"{self._n}{'/' if self._d != 1 else ''}{self._d if self._d != 1 else ''}"

    def __call__(self) -> float:
        return self._n / self._d

    def __getitem__(self, item):
        if item not in ["n", "d"]:
            return
        else:
            return self._n if item == "n" else self._d

    def __iter__(self):
        yield self._n
        yield self._d

    def __add__(self, other):
        if isinstance(other, int):
            return self + Rational(other)
        if isinstance(other, Rational):
            n1, d1 = self
            n2, d2 = other
            
            n = n1*d2 + n2*d1
            d = d1*d2

            return Rational(n, d)
    
    def __sub__(self, other):
        return self + -1*other

    def __mul__(self, other):
        if isinstance(other, int):
            return Rational(other * self._n, self._d)
        if isinstance(other, Rational):
            return Rational(self._n * other._n, self._d * other._d)

    def __truediv__(self, other):
        if isinstance(other, int):
            return self * Rational(1, other)
        if isinstance(other, Rational):
            return Rational(self._n * other._d, self._d * other._n)

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        if isinstance(other, int):
            return Rational(other) - self
        if isinstance(other, Rational):
            return other - self

    def __rmul__(self, other):
        return self * other

    def __rtruediv__(self, other):
        if isinstance(other, int):
            return Rational(other) / self
        if isinstance(other, Rational):
            return other / self

