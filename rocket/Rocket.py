import logging

from data.FlightData import FlightData
from gravity.gravity import calculate_gravity


class Rocket:
    def __init__(self):
        self.flight_data_history: [FlightData] = [
            FlightData(100, 100, 100,
                       [100, 100, 100],
                       [100, 100, 100],
                       [100, 100, 100]),
            FlightData(90, 100, 100,
                       [100, calculate_gravity(90), 100],
                       [100, 100, 100],
                       [100, 100, 100])
        ]
        self.parachute_released = False

    def last_data(self) -> FlightData:
        return self.flight_data_history[-1]

    def check_engine_shut_down(self) -> bool:
        """
        Verify whether the engine has ceased producing thrust by calculating the gravitational force at the current
        altitude and comparing it to the acceleration in the y-axis present in the flight data.

        Potential drag effects have been taken into account.

        Parachute can be deployed iff the engine has shut down.
        """
        # The <= is because of the drag effect
        acceleration_y = self.last_data().acceleration[1]
        gravity = calculate_gravity(self.last_data().altitude)
        if acceleration_y <= gravity:
            logging.warning(f"Engine shutdown detected -> ay={acceleration_y}m/s²")
            return True
        return False

    def check_altitude_decreasing(self) -> bool:
        """
        Check if the rocket started free-falling
        """
        if len(self.flight_data_history) < 2:
            return False
        altitude = self.last_data().altitude
        if altitude < self.flight_data_history[-2].altitude:
            logging.warning(f"Altitude decreasing -> h={altitude}m")
            return True
        return False

    def check_pointing_downwards(self) -> bool:
        """
        Release the parachute iff the tilt angle is >= 90 degrees
        """
        alpha_y = self.last_data().position_angles[1]
        if alpha_y >= 90:
            logging.warning(f"Attitude pointing downwards -> αy={alpha_y}º")
            return True
        return False

    def release_parachute(self):
        self.parachute_released = True
        logging.warning("Parachute deployment confirmed")
