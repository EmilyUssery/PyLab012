import turtle
from typing import List


class Sun:
    def __init__(self, name: str, radius: float, mass: float, temp:float, x:int, y:int, icon:str):
        self.__name = name
        self.__radius = radius
        self.__mass = mass
        self.__temp = temp
        self.__x = x
        self.__y = y
        # turtle stuff
        self._t = turtle.Turtle()
        self._t.color("yellow")
        self._t.shape("circle")
        self._t.goto(self.__x, self.__y)
        self._icon = icon


    def get_mass(self) -> float:
        return self.__mass

    def get_x_pos(self):
        return self.__x

    def get_y_pos(self):
        return self.__y
    def update(self,obj, event:str):
        obj.get_screen().addshape(self._icon)
        self._t.shape(self._icon)


    def __str__(self):
        return f"Sun(name={self.__name}, mass={self.__mass})"