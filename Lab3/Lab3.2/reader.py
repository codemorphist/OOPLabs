from equation import *


class ReaderEquationsData:
    def __init__(self, filepath: str):
        self._filepath = filepath
        self._readed = False
    
        self._by_solutions = [
            [ ], # no one solution
            [ ], # one solution
            [ ], # two solutions
            [ ], # three solutions
            [ ], # four solutions
            [ ], # all real solutions
        ]

        self._min_solution = None
        self._min_solution_eq = None

        self._max_solution = None
        self._max_solution_eq = None

    def __create_equation__(self, params: list[int]) -> Equation:
        if len(params) == 2:
            return Equation(*params)
        elif len(params) == 3:
            return QuadraticEquation(*params)
        elif len(params) == 5:
            a, _, b, _, c = params
            return BiQuadraticEquation(a, b, c)
        else:
            print(params)
            raise Exception("Too many or no one parameters to create equation")

    def __analyse_equation__(self, eq: Equation) -> None:
        solvs = eq.solve()
        if solvs == REAL:
            self._by_solutions[5].append(eq)
            return 
        else:
            self._by_solutions[len(solvs)].append(eq)

        if len(solvs) != 1:
            return
        for s in solvs:
            if self._min_solution is None or s < self._min_solution:
                self._min_solution = s
                self._min_solution_eq = eq
            elif self._max_solution is None or s > self._max_solution:
                self._max_solution = s
                self._max_solution_eq = eq

    def read(self) -> None:
        file = open(self._filepath, "r") 
        for line in file:
            line = line.strip().split()
            params = list(map(int, line))

            if params != []:
                eq = self.__create_equation__(params)
                self.__analyse_equation__(eq)

        self._readed = True

    @property
    def data(self):
        if not self._readed:
            raise Exception("Data from file not readed")

        return [
            self._by_solutions,
            (self._min_solution, self._min_solution_eq),
            (self._max_solution, self._max_solution_eq)
        ]


