class Triangle:
    def __init__(self, x1, y1, x2, y2):
        self.position = (0, 0)  # absolute position for first vertex
        self.vertex1 = (x1, y1) # position for second vertex
        self.vertex2 = (x2, y2) # position for third vertex
        self.color: tuple[int] | str = (255, 255, 255) # tringle color     

    def set_position(self, x, y):
        self.position = (x, y)

    def set_color(self, color):
        self.color = color
