from simulation import Simulation
from planet import Planet
from solar_system import SolarSystem
from sun import Sun



def main():
    solar_system = SolarSystem()
    solar_system.add_sun(Sun(name="My Sun", radius=5, mass=100, temp = 1000, x = 200, y =200))
    solar_system.add_planet(Planet(name = "Hello World", radium = 17, mass = .560, distance = 2, temp = 200, x = 5,y = 6, vel_x = 100, vel_y = 20))
    sim = Simulation(solar_system ,500, 500,100)
    solar_system.show_planets()
    sim.run()
    solar_system.show_planets()

if __name__ == "__main__": main()

