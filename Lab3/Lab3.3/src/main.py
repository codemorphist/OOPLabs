from reader import *


def print_result(r: ReaderFiguresData):
    print()
    print(r._filepath, "-"*(30 - len(r._filepath)))
    r.read()
    print("Max volume figure:")
    print("Figure:", r.get_result())
    print("Volume:", r._max_volume)
    print("-"*30)


r1 = ReaderFiguresData("../test_data/input01.txt")
r2 = ReaderFiguresData("../test_data/input02.txt")
r3 = ReaderFiguresData("../test_data/input03.txt")

print_result(r1)
print_result(r2)
print_result(r3)


