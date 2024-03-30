from reader import *

def print_info(data: ReaderFiguresData):
    if not data.readed:
        print("You dont read data from file.")

    fig, perim, area = data.get_result()
    filename = data.filepath
    print(f"[{filename}]","-"*(60 - len(filename)-3))
    if fig is None:
        print("None any max figure in file")
    else:
        print(fig, "\n")
        print("Max perimeter:", perim)
        print("Max area:", area)
    print("-"*60, "\n")


data1 = ReaderFiguresData("../test_data/input01.txt")
data2 = ReaderFiguresData("../test_data/input02.txt")
data3 = ReaderFiguresData("../test_data/input03.txt")
data4 = ReaderFiguresData("../test_data/input04.txt")

data1.read()
data2.read()
data3.read()
data4.read()

print_info(data1)
print_info(data2)
print_info(data3)
print_info(data4)
