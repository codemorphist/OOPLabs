from rational import Rational
from calculator import calculate_hack


class ExpressionReader:
    def __init__(self, filename: str):
        self._filename = filename
        self._result = []

    def result(self) -> list[Rational]:
        return self._result

    def read(self) -> None:
        with open(self._filename, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                self._result.append(calculate_hack(line))


