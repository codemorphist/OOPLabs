from triangle import Triangle
from drawer import Drawer, Coord, Angle
from time import sleep
from math import pi


def draw_100_triangles():
    # draw 100 random triangles
    d = Drawer()
    for i in range(100):
        tr = d.get_random_triangle()
        d.draw_triangle(tr)

    input()


def animate_rotation(tr: Triangle, angle: Angle):
    d = Drawer()
    
    r = 0

    while r < angle:
        d.clear()
        tr.set_rotation(r)
        d.draw_triangle(tr)
        sleep(0.1)
        r += 0.1

    input()

def animate_rotation_of_dot(tr: Triangle, angle: Angle, dot: Coord):
    tr.set_pivot(*dot)
    animate_rotation(tr, angle)


def animate_scale(tr: Triangle, 
                  scale: tuple[int] | tuple[float]):
    d = Drawer()

    sx, sy = scale

    tsx, tsy = 1, 1
    while tsx < sx:
        d.clear()
        tr.set_scale(tsx, tsy)
        d.draw_triangle(tr)
        tsx += 1
        sleep(0.3)

    while tsy < sy:
        d.clear()
        tr.set_scale(tsx, tsy)
        d.draw_triangle(tr)
        tsy += 1
        sleep(0.3)

    input()


def animate_scale_of_dot(tr: Triangle, 
                         scale: tuple[int] | tuple[float],
                         dot: Coord):
    tr.set_pivot(*dot)
    animate_scale(tr, scale)


animate_scale_of_dot(Triangle(40, 50, 60, -50), (4, 4), (10, 16))
