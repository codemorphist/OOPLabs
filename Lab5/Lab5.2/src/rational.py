from math import gcd


class Rational:
    def __new__(cls, *args):
        if len(args) > 2:
            raise Exception(f"Too many arguments for Rational number")
        if len(args) < 1:
            raise Exception(f"Not enought arguments for Rational number")

        self = super().__new__(cls)

        # ----------------------------------
        # if str representation
        if isinstance(args[0], str):
            if len(args) > 1:
                raise Exception(f"Too many arguments for Rational number")

            cls.__from_string__(self, args[0])
            return self

        # ----------------------------------
        # if int representation
        for val in args:
            if not isinstance(val, int):
                raise Exception(f"Not valid type parameter ({val}) for Rational number")
        cls.__from_nums__(self, *args)

        return self

    def __from_string__(self, rstr: str) -> None:
        """
        Initialize Rational class from string, like:
        2/3, 4, 1/3, ...

        :param rstr: Rational number string representation
        """
        n, d = self.__parse__(rstr) 
        self.__from_nums__(n, d)
        
    def __from_nums__(self, n: int, d: int=1) -> None:
        """
        Initialize Rational class from integer parameters

        :param n: Numerator
        :param d: Denumerator
        """
        if d == 0:
            raise ZeroDivisionError("Zero division in Rational number")

        if d < 0:
            d = abs(d)
            n = -n

        self._n = n
        self._d = d

        self.__simplify__()

    def __parse__(self, rstr: str) -> tuple[int, int]:
        """
        Parse Numerator and Denumerator from Rational number
        string representation

        :param rstr: Rational number string representation
        :return: Tuple of (Numerator: int, Denumerator: int)
        """
        valid = self.__validate__(rstr)
        if not valid:
            raise Exception(f"Not valid Rational number representation: `{rstr}`")

        rstr = rstr.replace(" ", "")
        n, d = None, 1
        if "/" in rstr:
            a, b = rstr.split("/")
            n = int(a)
            d = int(b)
        else:
            n = int(rstr)

        return n, d

    def __validate__(self, rstr: str) -> bool:
        """
        This fucntion validate correct Rational number 
        in string representation: N/D

        :param rstr: Rational number string representation
        :return: Valid of invalid string representation
        """
        if rstr.count("/") > 1:
            return False

        slash = False
        for ch in rstr:
            if ch not in ["/", " ", "-"] and not ch.isnumeric():
                return False
            if ch == "/":
                slash = True
            if slash and ch.isnumeric():
                slash = False
        return True and not slash    
    
    def __repr__(self) -> str:
        return f"Rational{self._n, self._d}"

    def __simplify__(self) -> None:
        """
        Simplify Rational number, divide 
        N and D by GDC(N, D)
        """
        n, d = self
        if n == 0:
            self._d = 1
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
            raise KeyError(f"Invalid key: {item}")
        else:
            return self._n if item == "n" else self._d

    def __setitem__(self, item: str, value: int):
        if item not in ["n", "d"]:
            raise KeyError(f"Invalid key: {item}")
        else:
            if item == "d" and value == 0:
                raise ZeroDivisionError("Zero division in Rational number")
            elif not isinstance(value, int):
                raise ValueError(f"Can't set {value} as value of Rational number")
            else:
                if item == "d": self._d = value
                else: self._n = value

    @property
    def n(self) -> int:
        """Return Numerator"""
        return self._n

    @property
    def d(self) -> int:
        """Return Denumerator"""
        return self._d

    def __iter__(self):
        """
        Unpack Rational number like tuple:
        n, d = Rational(n, d)
        """
        yield self._n
        yield self._d

    def __add__(self, other):
        if isinstance(other, int):
            return self + Rational(other)
        elif isinstance(other, Rational):
            n1, d1 = self
            n2, d2 = other
            
            n = n1*d2 + n2*d1
            d = d1*d2

            return Rational(n, d)
        else:
            raise TypeError(f"Can't add {type(other).__name__} to Rational")
    
    def __sub__(self, other):
        return self + -1*other

    def __mul__(self, other):
        if isinstance(other, int):
            return Rational(other * self._n, self._d)
        elif isinstance(other, Rational):
            return Rational(self._n * other._n, self._d * other._d)
        else:
            raise TypeError(f"Can't multiply {type(other).__name__} and Rational")

    def __truediv__(self, other):
        if isinstance(other, int):
            return self * Rational(1, other)
        elif isinstance(other, Rational):
            return Rational(self._n * other._d, self._d * other._n)
        else:
            raise TypeError(f"Can't divide Rational on {type(other).__name__}")

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        if isinstance(other, int):
            return Rational(other) - self
        elif isinstance(other, Rational):
            return other - self
        else:
            raise TypeError(f"Can't subtitude Rational from {type(other).__name__}")

    def __rmul__(self, other):
        return self * other

    def __rtruediv__(self, other):
        if isinstance(other, int):
            return Rational(other) / self
        elif isinstance(other, Rational):
            return other / self
        else:
            raise TypeError(f"Can't divide {type(other).__name__} on Rational")

