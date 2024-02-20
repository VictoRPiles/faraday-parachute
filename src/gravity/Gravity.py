__author__ = "Víctor Piles"
__email__ = "vpildel@upv.edu.es"
__date__ = "20/02/2024"

G_const = 6.67430e-11  # Gravitational constant in m^3/kg/s^2
M_earth = 5.972e24  # Mass of the Earth in kg
R_earth = 6371000  # Radius of the Earth in meters


class Gravity:

    @staticmethod
    def calculate_gravity(altitude) -> float:
        """
        Calculate gravity from the center of the Earth to the rocket's position
        """
        # noinspection PyPep8Naming
        R = R_earth + altitude
        g = -((G_const * M_earth) / (R ** 2))
        return g
