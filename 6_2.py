class Road:
    __mass_1cm = 25
    __thickness = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calculator(self):
        mass = self._length * self._width * Road.__mass_1cm * Road.__thickness / 1000
        print(f"{mass} tone")


example = Road(5000, 20)
example.mass_calculator()
