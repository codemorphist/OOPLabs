from figures import Figure
from figures import *
from figures import Len, Area

class ReaderFiguresData:
    def __init__(self, filepath: str):
        self._filepath = filepath 
        self._max_volume = 0
        self._max_volume_figure = None
        self._readed = False

    @property
    def max_volume_figure(self) -> Figure:
        return self._max_volume_figure

    def max_figure(self, fig: Figure):
        if fig is None:
            return 

        volume = fig.volume()
        if volume > self._max_volume:
            self._max_volume_figure = fig
            self._max_volume = volume

    def __create_figure__(self, name: str, params: list[Len]) -> Figure:
        try:
            class_ = globals()[name]
            instance = class_(*params)
            return instance
        except KeyError:
            print(f"Figure {name} not exist!")
            return None

    def read(self) -> None:
        file = open(self._filepath, "r") 
        for line in file:
            line = line.strip().split()
            name = line[0]
            params = list(map(int, line[1:]))

            fig = self.__create_figure__(name, params)
            
            self.max_figure(fig)

        self.readed = True


    def get_result(self) -> Figure:
        if not self.readed:
            raise Exception("You don't read data yet.")
       
        return self.max_volume_figure
