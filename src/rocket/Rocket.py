__author__ = "Víctor Piles"
__email__ = "vpildel@upv.edu.es"
__date__ = "19/02/2024"

import logging

from gravity.Gravity import Gravity
from src.data.FlightData import FlightData


class Rocket:
    def __init__(self):
        self.flight_data_history: [FlightData] = []
        self.engine_on = None
        self.attitude_upwards = None
        self.parachute_released = False

    def last_data(self) -> FlightData:
        return self.flight_data_history[-1]

    def check_engine_shut_down(self) -> bool:
        """
        Verify whether the engine has ceased producing thrust by calculating the gravitational force at the current
        altitude and comparing it to the acceleration in the y-axis present in the flight data.

        Potential drag effects and uncertainties have been taken into account.

        Parachute can be deployed iff the engine has shut down.
        """
        # The <= is because of the drag effect
        acceleration_y = self.last_data().acceleration[1]
        # Added uncertainty for reliability reasons
        uncertainty = 0.5
        gravity = Gravity.calculate_gravity(self.last_data().altitude)
        if (gravity - uncertainty) <= acceleration_y <= (gravity + uncertainty):
            if self.engine_on:
                logging.warning(f"Engine shutdown detected -> ay={acceleration_y}m/s²")
                self.engine_on = False
            return True
        # Check if the engine was off and then turned on (for ignition)
        elif not self.engine_on:
            logging.warning(f"Engine startup detected -> ay={acceleration_y}m/s²")
        self.engine_on = True
        return False

    def check_altitude_decreasing(self) -> bool:
        """
        Determine if the rocket's altitude is decreasing by contrasting its previous altitude with the current one.

        For enhanced reliability, both altimeter readings and GPS coordinates are employed.
        """
        if len(self.flight_data_history) < 2:
            return False
        altitude = self.last_data().altitude
        altitude_gps = self.last_data().gps_coordinates[1]
        altitude_decreasing = altitude < self.flight_data_history[-2].altitude
        altitude_decreasing_gps = altitude_gps < self.flight_data_history[-2].gps_coordinates[1]
        if altitude_decreasing & altitude_decreasing_gps:
            logging.warning(f"Altitude decreasing -> h={altitude}m")
            return True
        return False

    def check_pointing_upwards(self) -> bool:
        """
        To ensure that the parachute deployment occurs when the rocket is in a stable descent orientation, deploy the
        parachute only if the tilt angle is between 30 and 150 degrees.
        """
        theta = self.last_data().position_angles[1]
        if 30 <= theta <= 150:
            if not self.attitude_upwards:
                logging.warning(f"Attitude pointing upwards -> θy={theta}º")
                self.attitude_upwards = True
        elif self.attitude_upwards:
            logging.warning(f"Attitude pointing downwards -> θy={theta}º")
            self.attitude_upwards = False
        return self.attitude_upwards

    def release_parachute(self) -> None:
        self.parachute_released = True
        logging.warning("Parachute deployment confirmed")
