from rational import Rational
from rational_list import RationalList


class RationalListReader:
    def __init__(self, filename: str):
        self._filename = filename
        self._list = []

    def result(self) -> list[Rational]:
        return self._list

    def read(self) -> None:
        with open(self._filename, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                rlist = RationalList([])
                for num in line.split("  "):
                    rlist += Rational(num)
                self._list.append(rlist)



