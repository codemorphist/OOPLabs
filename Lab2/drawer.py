from turtle import *
from random import randint
from triangle import Triangle


class Drawer:
    def __init__(self):
        clearscreen()
        speed(0)
        colormode(255) 
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

    def get_random_color(self) -> tuple[int]:
        """
        :return random color in format (int, int, int)
        """
        return (randint(0,255), randint(0,255), randint(0,255))

    def get_random_vertex(self, 
                            x_range: tuple[int] = (-350, 350),
                            y_range: tuple[int] = (-350, 350)) -> tuple[int]:
        """
        Return random 2D vector

        :param x_range - x random range <from> to <to> for vertex
        :param y_range - y random range <from> to <to> for vertex

        :return random vector 
        """
        return (randint(*x_range), randint(*y_range))

    def get_random_triangle(self, 
                            x_range: tuple[int] = (-350, 350),
                            y_range: tuple[int] = (-350, 350)) -> Triangle:
        """
        Return random Triangle instance, with random color and position

        :param x_range - x random range <from> to <to> for vertex
        :param y_range - y random range <from> to <to> for vertex

        :return Triangle with random position, vertex1, vertex2
        """
        tr = Triangle(
            *self.get_random_vertex(x_range, y_range),
            *self.get_random_vertex(x_range, y_range)
        )
        tr.set_position(*self.get_random_vertex(x_range, y_range))
        tr.set_color(self.get_random_color())

        return tr
        

