from oop.Geometry.figure import Figure


class Circle(Figure):
    def __init__(self, color, pointx, pointy, radius):
        self.__radius = radius
        super().__init__(color, pointx, pointy)

    def set_color(self, color):
        super().set_color(color)

    def set_pointx(self, pointx):
        super().set_pointx(pointx)

    def get_pointx(self):
        return super().get_pointx()

    def set_pointy(self, pointy):
        super().set_pointy(pointy)

    def get_pointy(self):
        return super().get_pointy()

    def get_color(self):
        return super().get_color()

    def set_radius(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius
