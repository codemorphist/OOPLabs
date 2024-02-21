from figures import Figure, Triangle, Rectangle, Trapeze, Parallelogram, Circle
from figures import Len, Area

class ReadFiguresData:
    def __init__(self, filepath: str):
        self.filepath = filepath 

        self._max_perimeter_figure: Figure = None
        self._max_area_figure: Figure = None

        self._max_perimeter: Len = -1
        self._max_area: Area = -1

        self.readed = False


    @property
    def max_perimeter_figure(self) -> Figure:
        return self._max_perimeter_figure
    @max_perimeter_figure.setter
    def max_perimeter_figure(self, fig: Figure):
        perim = fig.get_perimeter
        if perim > self._max_perimeter:
            self._max_perimeter_figure = fig 
            self._max_perimeter = perim


    @property
    def max_area_figure(self) -> Figure:
        return self._max_area_figure
    @max_area_figure.setter
    def max_area_figure(self, fig: Figure):
        area = fig.get_area
        if area > self._max_area:
            self._max_area_figure = fig
            self._max_area = area


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

            print(name, params)
            
            self.max_perimeter_figure = fig
            self.max_area_figure = fig

        readed = True


    def get_result(self) -> None:
        if not self.readed:
            raise Exception("You don't read data yet.")
        
        return (self.max_perimeter_figure, 
                self.max_area_figure)
