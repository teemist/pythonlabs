from oop.Geometry.figure import Figure


class Rectangle(Figure):
    def __init__(self, width, height, color, pointx, pointy):
        super().__init__(color, pointx, pointy)
        self.__width = width
        self.__height = height

    def get_width(self, width):
        if width > 0:
            self.__width = width
        else:
            raise ValueError

    def get_height(self, height):
        if height > 0:
            self.__height = height
        else:
            raise ValueError
        
    # def set_pointx(self, x):
    #     super().set_pointx(x)
    #
    # def get_pointx(self):
    #     super().get_pointx()
    #
    # def set_pointy(self, y):
    #     super().set_pointy(y)
    #
    # def get_pointy(self):
    #     super().get_pointy()
    #
    def area(self):
        return self.__width * self.__height
