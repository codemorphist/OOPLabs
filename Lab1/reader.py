from figures import Figure, Triangle, Rectangle, Trapeze, Parallelogram, Circle
from figures import Len, Area

class ReaderFiguresData:
    def __init__(self, filepath: str):
        self.filepath = filepath 

        self._max_perimeter_figure: Figure = None
        self._max_area_figure: Figure = None

        self.max_perimeter: Len = -1
        self.max_area: Area = -1

        self.readed = False


    @property
    def max_perimeter_figure(self) -> Figure:
        return self._max_perimeter_figure

    @max_perimeter_figure.setter
    def max_perimeter_figure(self, fig: Figure):
        perim = fig.perimeter
        if perim > self.max_perimeter:
            self._max_perimeter_figure = fig 
            self.max_perimeter = perim


    @property
    def max_area_figure(self) -> Figure:
        return self._max_area_figure

    @max_area_figure.setter
    def max_area_figure(self, fig: Figure):
        area = fig.area
        if area > self.max_area:
            self._max_area_figure = fig
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
            
            self.max_perimeter_figure = fig
            self.max_area_figure = fig

        readed = True


    def get_result(self) -> None:
        if not self.readed:
            raise Exception("You don't read data yet.")
        
        return (self.max_perimeter_figure, 
                self.max_area_figure)
