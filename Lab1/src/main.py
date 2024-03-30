from reader import *
import os.path

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


filepath = input("Input path to file with figures: ")
while not os.path.isfile(filepath):
    print(f"{filepath} is not file or not exist!")
    filepath = input("Try input path to file again: ")

data = ReaderFiguresData(filepath)
data.read()
print_info(data)

