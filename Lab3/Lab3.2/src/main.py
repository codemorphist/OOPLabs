from reader import ReaderEquationsData

def print_data(filename: str):
    reader = ReaderEquationsData(filename)
    reader.read()
    data = reader.data
        
    # no one solutions
    print("Equations without any solution:")
    for e in data[0][0]:
        print("\t", e)
    print()

    # one solution
    print("Equations with one solution:")
    for e in data[0][1]:
        print("\t", e)
    print()

    # two solutions
    print("Equations with two solutions:")
    for e in data[0][2]:
        print("\t", e)
    print()

    # three solutions
    print("Equations with three solution:")
    for e in data[0][3]:
        print("\t", e)
    print()

    # four solutions
    print("Equations with four solutions:")
    for e in data[0][4]:
        print("\t", e)
    print()

    # infty solution
    print("Equations with any solutions:")
    for e in data[0][5]:
        print("\t", e)

    print("\n\n")

    print("Min solution:", data[1][0])
    print("Min solution equation:", data[1][1])

    print()

    print("Max solution:", data[2][0])
    print("Max solution equation:", data[2][1])

    
f = input()
print_data(f)


