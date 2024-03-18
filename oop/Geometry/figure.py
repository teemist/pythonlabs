class Figure:
    def __init__(self, color, pointx, pointy):
        self.__color = color
        self.__pointx = pointx
        self.__pointy = pointy

    def set_color(self, color):
        if type(color) is str:
            self.__color = color
        else:
            raise ValueError("Цвет должен быть указан в виде строки")

    def get_color(self):
        return self.__color

    def set_pointx(self, pointx):
        self.__pointx = pointx

    def get_pointx(self):
        return self.__pointx

    def set_pointy(self, pointy):
        self.__pointy = pointy

    def get_pointy(self):
        return self.__pointy

    def move_to(self, x, y):
        self.set_pointx(int(x))
        self.set_pointy(int(y))
