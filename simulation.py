from solar_system import SolarSystem

class Simulation:
    def __init__(self, solar_system, width: int, height: int, num_periods: int):
        self._solar_system = solar_system
        self._width = width
        self._height = height
        self._num_periods = num_periods

    def run(self):
        print("Starting simulation...")
        for _ in range(self._num_periods):
            self._solar_system.move_planets()
        print("Simulation complete.")
        self._solar_system.show_planets()

