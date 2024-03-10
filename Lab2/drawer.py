from typing import TypeAlias

from turtle import *
from random import randint
from math import pi, sin, cos

from triangle import Triangle


Coord: TypeAlias = tuple[int] | tuple[float]
Angle: TypeAlias = float
Color: TypeAlias = tuple[int]


class Drawer:
    def __init__(self):
        clearscreen()
        speed(0)
        penup()
        setpos(0, 0)
        setheading(0)
        pendown()

    def clear(self):
        clearscreen()

    def draw_vector(self, 
                    start: Coord, 
                    end: Coord,
                    color: Color = (0, 0, 0)):
        penup()
        setheading(0)
        setpos(start)
        pendown()
        setpos(end)

    def draw_triangle(self, tr: Triangle):
        colormode(255) 
        speed(0)

        pos = tr.position
        col = tr.color

        # rotate vertex
        v0 = self.rotate_vertex(tr.position,
                                tr.rotation,
                                tr.pivot)
        v1 = self.rotate_vertex(tr.vertex1, 
                                tr.rotation, 
                                tr.pivot)
        v2 = self.rotate_vertex(tr.vertex2, 
                                tr.rotation, 
                                tr.pivot)

        # scale vertex
        v1 = self.scale_vertex(v1, *tr.scale)
        v2 = self.scale_vertex(v2, *tr.scale)

        penup()
        color(col)
        pendown()

        self.draw_vector(v0, v1)
        self.draw_vector(v0, v2)
        self.draw_vector(v1, v2)

    def rotate_vertex(self, 
                      vertex: Coord, 
                      angle: Angle,
                      pivot: Coord = (0, 0)) -> Coord:
        """
        Roatate 2D vertex to given angle of pivot

        :param vertex vertex to rotate
        :param rotation angle to rotate 

        :return rotated vertex
        """
        px, py = pivot
        x, y = vertex
        x, y = x - px, y - py
        return (
            x*cos(angle) - y*sin(angle) + px,
            x*sin(angle) + y*cos(angle) + py 
        )
        

    def scale_vertex(self, 
                     vertex: Coord, 
                     scale_x: int = 1, 
                     scale_y: int = 1) -> Coord:
        """
        Scale vertex by Ox and Oy

        :param vertex vertex to scale
        :param scale_x scale for Ox
        :param scale_y scala for Oy

        :return scaled vertex
        """
        return (vertex[0]*scale_x, vertex[1]*scale_y)


    def get_random_color(self) -> Color:
        """
        Generate random color

        :return random color in format (int, int, int)
        """
        return (randint(0,255), randint(0,255), randint(0,255))

    def get_random_vertex(self, 
                            x_range: tuple[int] = (-350, 350),
                            y_range: tuple[int] = (-350, 350)) -> Coord:
        """
        Generate random 2D vector

        :param x_range - x random range <from> to <to> for vertex
        :param y_range - y random range <from> to <to> for vertex

        :return random vector 
        """
        return (randint(*x_range), randint(*y_range))

    def get_random_triangle(self, 
                            x_range: tuple[int] = (-350, 350),
                            y_range: tuple[int] = (-350, 350)) -> Triangle:
        """
        Generate random Triangle instance, with random color and position

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
        

