from reader import *

def print_info(data: ReaderFiguresData):
    filename = data.filepath
    print(f"[{filename}]","-"*(60 - len(filename)-3))
    print("Max perimeter:", data.max_perimeter)
    print(data.max_perimeter_figure, "\n")
    print("Max area:", data.max_area)
    print(data.max_area_figure)
    print("-"*60, "\n")


data1 = ReaderFiguresData("./test_data/input01.txt")
data2 = ReaderFiguresData("./test_data/input02.txt")
data3 = ReaderFiguresData("./test_data/input03.txt")

data1.read()
data2.read()
data3.read()

print_info(data1)
print_info(data2)
print_info(data3)

