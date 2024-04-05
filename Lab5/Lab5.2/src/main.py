from reader import RationalListReader


# r1 = RationalListReader("../test_data/input01.txt")
r1 = RationalListReader("../test_data/input02.txt")
# r1 = RationalListReader("../test_data/input03.txt")

r1.read()

print("-"*20)
print(*r1.result(), sep="\n")
print("-"*20)
