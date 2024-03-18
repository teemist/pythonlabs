class Vehicle:
    def __init__(self, color, model, power, year):
        self.color = color
        self.model = model
        self.power = power
        self.year = year

    def set_year(self, year):
        self.year = year
    def get_year(self):
        return self.year
    def set_color(self, color):
        self.color = color
    def get_color(self):
        return self.color
    def set_model(self, model):
        self.model = model
    def get_model(self):
        return self.model
    def set_drive(self, power):
        self.power = power
    def get_power(self):
        return self.power

    def drive(self, direction):
        print("Driving to ", direction)
