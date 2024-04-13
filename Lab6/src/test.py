from rational_list import RationalList
from rational import Rational
    

arr = RationalList([Rational("2/3"), 3, 4, 4])

print(arr[0].n, arr[1].d)

for i in arr:
    print(i, end="  ")
print()


for j in arr:
    arr.pop()
    print(j, end="  ")
print()

print(arr)
