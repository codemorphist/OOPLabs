class Triangle:
    def __init__(self, x1, y1, x2, y2):
        self.position = (0, 0)  # absolute position for first vertex
        self.vertex1 = (x1, y1) # position for second vertex
        self.vertex2 = (x2, y2) # position for third vertex
        self.color: tuple[int] | str = (0, 0, 0) # tringle color     

        self.rotation = 0
        self.scale = (1, 1)
        self.pivot = self.position

    def set_position(self, x, y):
        self.position = (x, y)

    def set_color(self, color):
        self.color = color

    def set_rotation(self, rotation): # rotation in radians
        self.rotation = rotation

    def set_scale(self, scale_x, scale_y):  
        self.scale = (scale_x, scale_y) 

    def set_pivot(self, pivot_x, pivot_y):
        self.pivot = (pivot_x, pivot_y)
