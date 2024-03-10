from drawer import Drawer 
from math import pi

d = Drawer()

tr = d.get_random_triangle()
d.draw_triangle(tr)

tr.set_rotation(pi/2)
d.draw_triangle(tr)

input()
