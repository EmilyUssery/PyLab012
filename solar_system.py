from sun import Sun
from planet import Planet
from gravity import UniversalGravity as U, UniversalGravity
import math
from typing import List

class SolarSystem:
    def __init__(self):
        self._the_sun: Sun = None
        self._planets: List[Planet] = []

    def add_sun(self, the_sun: Sun):
        self._the_sun = the_sun

    def add_planet(self,new_planet: Planet):
        self._planets.append(new_planet)

    def show_planets(self):
        for planet in self._planets:
            print(planet)

    def move_planets(self, dt: float = 60 * 60):
        dt = .1 # Constant time interval for each solar system iteration.

        for planet in self._planets:
            # Move the distance covered in the interval dt
                planet.move_to(
                    planet.get_x_pos() + dt * planet.get_vel_x(),
                    planet.get_y_pos() + dt * planet.get_vel_y())

                # After move we need to calculate the new distance from the sun using the distance formula.
                dist_x = self._the_sun.get_x_pos() - planet.get_x_pos()
                dist_y = self._the_sun.get_y_pos() - planet.get_y_pos()
                new_distance = math.sqrt(dist_x ** 2 + dist_y ** 2)

                # Let's calculate our new acceleration so we can set our new velocity
                acc_x = U.G * self._the_sun.get_mass() * dist_x / new_distance ** 3
                acc_y = U.G * self._the_sun.get_mass() * dist_y / new_distance ** 3

                # Now let's calculate the new x and y velocities and update them for the planet
                planet.set_vel_x(planet.get_vel_x() + dt * acc_x)
                planet.set_vel_y(planet.get_vel_y() + dt * acc_y)

