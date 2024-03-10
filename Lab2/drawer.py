from turtle import *
from triangle import Triangle


class Drawer:
    def __init__(self):
        clearscreen()
        penup()
        setpos(0, 0)
        setheading(0)
        pendown()

    def draw_triangle(self, tr: Triangle):
        pos = tr.position
        v1 = tr.vertex1
        v2 = tr.vertex2
        col = tr.color

        penup()
        color(col)
        setpos(pos)
        pendown()
        setpos(v1)
        setpos(v2)
        setpos(pos)

