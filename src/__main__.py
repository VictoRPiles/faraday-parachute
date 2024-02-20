import logging
import sys
import time

from data.FlightData import sample_flight_data
from rocket.Rocket import Rocket


def main():
    logging.info("Faraday Rocketry parachute deployment system activated")

    rocket = Rocket()

    logging.debug("Generating sample data...")
    index = 0
    while not rocket.parachute_released:
        # Throw an error if no sample data was provided. For testing purposes.
        if len(sample_flight_data) <= index:
            logging.error("Not enough sample data provided")
            sys.exit(1)

        rocket.flight_data_history.append(sample_flight_data[index])

        logging.info(rocket.last_data())
        if rocket.check_engine_shut_down() & rocket.check_altitude_decreasing() & rocket.check_pointing_downwards():
            rocket.release_parachute()

        index += 1
        # Simulate data being updated every second
        time.sleep(1)


if __name__ == '__main__':
    main()
