import logging

from logger.LoggerFormatter import configure_logger
from rocket.Rocket import Rocket

if __name__ == '__main__':
    configure_logger()
    logging.info("Faraday Rocketry parachute deployment system activated")

    rocket = Rocket()
    logging.info(rocket.last_data())
    if rocket.check_engine_shut_down() & rocket.check_altitude_decreasing() & rocket.check_pointing_downwards():
        rocket.release_parachute()
