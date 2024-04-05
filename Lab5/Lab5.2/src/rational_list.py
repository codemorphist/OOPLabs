from rational import Rational
from copy import copy


class RationalList(list):
    def __init__(self, iterable: list[Rational | int]):
        items = self.__to_rational_list__(iterable)
        super().__init__(item for item in items)

    def __setitem__(self, index, item):
        if not self.__check_type__(item):
            raise TypeError(f"Not valid type ({type(item).__name__}) for Rational List")
        super().__setitem__(index, self.__to_rational__(item))

    def insert(self, index, item):
        if not self.__check_type__(item):
            raise TypeError(f"Not valid type ({type(item).__name__}) for Rational List")
        super().insert(index, self.__to_rational__(item))

    def append(self, item):
        if not self.__check_type__(item):
            raise TypeError(f"Not valid type ({type(item).__name__}) for Rational List")
        super().append(self.__to_rational__(item))

    def extend(self, other):
        if isinstance(other, RationalList):
            super().extend(other)
        else:
            items = self.__to_rational_list__(other) 
            super().extend(item for item in items)

    def __add__(self, other):
        new = copy(self)
        if isinstance(other, list):
            new.extend(other)
        else:
            new.append(other)
        return new

    def __iadd__(self, other):
        self = self + other
        return self

    def __to_rational__(self, item) -> Rational:
        """
        If item is Rational return Rational
        If item is int return Rational

        :param item: Rational or int
        :return: Rational number or None
        """
        if isinstance(item, int):
            return Rational(item)
        elif isinstance(item, Rational):
            return item
        else: # TODO: Raise Exception
            return None

    def __to_rational_list__(self, iterable) -> list[Rational]:
        """
        Convert list of Rational and int to list that
        contait only Rational numbers

        :param items: List of Rational or int
        :return: List of Rational numbers
        """
        items: list[Rational] = []

        if not isinstance(items, list):
            raise TypeError(f"{items} is not a list")

        for item in iterable:
            if not self.__check_type__(item):
                raise TypeError(f"Not valid type ({type(item).__name__}) `{item}`"\
                                " for Rational List")
            else:
                items.append(self.__to_rational__(item))
        return items
            
    def __check_type__(self, item) -> bool:
        """
        Check type of Rational and int

        :param item: Object
        :return: If Object is Rational or int
        """
        return isinstance(item, Rational) or isinstance(item, int)

