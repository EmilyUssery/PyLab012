from simulation import Simulation
from planet import Planet
from solar_system import SolarSystem
from sun import Sun



def main():
    solar_system = SolarSystem()
    the_sun = Sun(name="My Sun", radius=5, mass=1.989e14, temp = 5000, x = 0, y =0, icon="sun.gif")
    solar_system.add_sun(the_sun)
    solar_system.add_planet(Planet(name = "Earth", radium = 17, mass =.33,
                                distance = 50, x = 0,y = 50, vel_x = 15, vel_y = 5, color="blue"))
    solar_system.add_planet(Planet(name="Mars", radium=22.0 ,mass=.33,
                                   distance=50, x=0, y=100, vel_x=12, vel_y=5, color="red"))
    sim = Simulation(solar_system ,800, 800,5000)
    solar_system.show_planets()
    sim.register(the_sun)
    sim.run()
    solar_system.show_planets()

if __name__ == "__main__": main()

