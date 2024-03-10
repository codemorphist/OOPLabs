from drawer import Drawer

d = Drawer()

# draw 100 random triangles
for i in range(100):
    tr = d.get_random_triangle()
    d.draw_triangle(tr)

input()
