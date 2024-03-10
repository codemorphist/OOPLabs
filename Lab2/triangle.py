class Triangle:
    def __init__(self, x1, y1, x2, y2):
        self.position = (0, 0)   # абсолютна позиція першої вершини
        self.vertex1 = (x1, y1)  # позиція другої відносно першої вершини
        self.vertex2 = (x2, y2)  # позиція третьої відносно першої вершини
        self.color = "black"     # колір трикутника за промовчанням

    def set_position(self, x, y):
        self.position = (x, y)

    def set_color(self, color):
        self.color = color
