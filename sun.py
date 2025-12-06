class Sun:
    def __init__(self, name: str, radius: float, mass: float, temp:float, x:int, y:int):
        self.__name = name
        self.__radius = radius
        self.__mass = mass
        self.__temp = temp
        self.__x = x
        self.__y = y


    def get_mass(self) -> float:
        return self.__mass

    def get_x_pos(self):
        return self.__x

    def get_y_pos(self):
        return self.__y

    def __str__(self):
        return f"Sun(name={self._name}, mass={self._mass})"






