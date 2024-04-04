from reader import ExpressionReader

f1 = ExpressionReader("./test_data/input01.txt")
f1.read()
print(f1._filename, "-"*(30-len(f1._filename)))
print(*f1.result(), sep="\n")
print("-" * 30)

