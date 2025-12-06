import math
import turtle


class Planet:
    def __init__(self, name: str, radium: float, mass: float, distance: float, temp:float,
                 x: float,y: float, vel_x: float, vel_y: float):
        self.__name = name
        self.__radium = radium
        self.__mass = mass
        self.__distance = distance
        self.__temp = temp
        self.__x = x
        self.__y = y
        self.__vel_x = vel_x
        self.__vel_y = vel_y


    def get_mass(self) -> float:
        return self.__mass

    def get_x_pos(self) -> float:
        return self.__x

    def get_y_pos(self) -> float:
        return self.__y

    def get_vel_x(self) -> float:
        return self.__vel_x

    def get_vel_y(self) -> float:
        return self.__vel_y

    def set_vel_x(self, new_x_vel: float):
        self.__vel_x = new_x_vel

    def set_vel_y(self, new_y_vel: float):
        self.__vel_y = new_y_vel

    def move_to(self,new_x:float, new_y:float):
        self.__x = new_x
        self.__y = new_y

    def get_distance(self) -> float:
        """Distance from sun at (0,0)."""
        return math.sqrt(self.__x ** 2 + self.__y ** 2)

    def __str__(self) -> str:
        return f"Planet(name={self.__name}, mass={self.__mass}, x={self.__x}, y={self.__y})"


