import turtle
from solar_system import SolarSystem

class Simulation:
    def __init__(self, solar_system, width: int, height: int, num_periods: int):
        self._solar_system = solar_system
        self._width = width
        self._height = height
        self._num_periods = num_periods
        # Turtle stuff
        self._t = turtle.Turtle()
        self._t.hideturtle()
        self._screen = turtle.Screen()
        self._screen.setup(width=width, height=height)
        self._screen.bgcolor("black")
        self._t.clear()
        # Observer:list
        self.observer:list = []

    def register(self,observer):
        self.observer.append(observer)

    def notify(self,event:str):
        for observer in self.observer:
            observer.update(self,event)

    def get_screen(self):
        return self._screen

    def run(self):
        self.notify("STARTING")
        print("Starting simulation...")
        for _ in range(self._num_periods):
            self._solar_system.move_planets()
        print("Simulation complete.")
        self._solar_system.show_planets()
        self.freeze()


    def freeze(self):
        self._screen.exitonclick()


