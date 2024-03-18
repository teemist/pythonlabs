import vehicle
import garage
import computer
import mouse
from oop.Geometry import circle, rectangle

opel = vehicle.Vehicle("red", "opel", 140, 2008)
print(opel.get_year())
garage = garage.Garage()
garage.add(opel)
garage.show_cars()


mouse = mouse.Mouse("A4tech", 1300)
print(mouse.getinfo())

comp = computer.Computer("Admin", 2048, "Celeron", "Nvidia", None)
print(comp.getinfo())
print("Подключили мышку")
comp.connect_mouse(mouse)
print(comp.getinfo())
rect = rectangle.Rectangle(10, 10, "blue", 0, 0)
krug = circle.Circle("green", 10, 10, 5)
print(krug.get_color())
print(rect.get_pointx(), rect.get_pointy())
rect.move_to(3, 3)
print(rect.get_pointx(), rect.get_pointy())
print(rect.area())
