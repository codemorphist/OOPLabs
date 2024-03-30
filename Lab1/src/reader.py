from figures import Figure, Triangle, Rectangle, Trapeze, Parallelogram, Circle
from figures import Len, Area

class ReaderFiguresData:
    def __init__(self, filepath: str):
        self.filepath = filepath 

        self._max_figure: Figure = None

        self.max_perimeter: Len = -1
        self.max_area: Area = -1

        self.readed = False


    @property
    def max_figure(self) -> Figure:
        return self._max_figure

    @max_figure.setter
    def max_figure(self, fig: Figure):
        perim = fig.perimeter
        area = fig.area
        if area > self.max_area and perim > self.max_perimeter:
            self._max_figure = fig
            self.max_perimeter = perim
            self.max_area = area


    def __create_figure(self, name: str, params: list[Len]) -> Figure:
        try:
            class_ = globals()[name]
            instance = class_(*params)
            return instance
        except KeyError:
            print(f"Figure {name} not exist!")
            return None


    def read(self) -> None:
        file = open(self.filepath, "r") 
        for line in file:
            line = line.strip().split()
            name = line[0]
            params = list(map(int, line[1:]))

            fig = self.__create_figure(name, params)
            
            self.max_figure = fig

        self.readed = True


    def get_result(self) -> None:
        if not self.readed:
            raise Exception("You don't read data yet.")
        
        return (self.max_figure,
                self.max_perimeter,
                self.max_area)
