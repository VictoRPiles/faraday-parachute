from gravity.gravity import calculate_gravity


class FlightData:
    def __init__(self,
                 altitude: float, pressure: float, temperature: float,
                 acceleration: [float],
                 position_angles: [float],
                 gps_coordinates: [float]):
        self.altitude = altitude
        self.pressure = pressure
        self.temperature = temperature
        self.acceleration = acceleration
        self.position_angles = position_angles
        self.gps_coordinates = gps_coordinates

    def __str__(self) -> str:
        return str({
            "altitude": self.altitude,
            "pressure": self.pressure,
            "temperature": self.temperature,
            "acceleration": self.acceleration,
            "position_angles": self.position_angles,
            "gps_coordinates": self.gps_coordinates,
        })


# Sample data for testing purposes
sample_flight_data: [FlightData] = [
    # Launch simulation
    FlightData(0, 101325, 288, [0, calculate_gravity(0), 0], [0, 0, 0], [0, 0, 0]),
    # Flight simulation
    FlightData(50, 101200, 287.5, [0, 9.800, 0], [0, 0, 0.5], [0, 0, 50]),
    FlightData(100, 101100, 287.0, [0, 10.20, 0], [0, 1, 1], [0, 0, 100]),
    FlightData(200, 100900, 286.5, [0, 10.50, 0], [0, 1.5, 2], [0, 0, 200]),
    FlightData(300, 100700, 286.0, [0, 10.80, 0], [0, 2, 3], [0, 0, 300]),
    FlightData(500, 100500, 285.5, [0, 11.20, 0], [0, 2.5, 4], [0, 0, 500]),
    FlightData(700, 100300, 285.0, [0, 11.50, 0], [0, 3, 5], [0, 0, 700]),
    FlightData(1000, 10000, 284.5, [0, 11.90, 0], [0, 3.5, 6], [0, 0, 1000]),
    FlightData(1500, 99500, 284.0, [0, 12.30, 0], [0, 4, 7], [0, 0, 1500]),
    FlightData(2000, 99000, 283.5, [0, 12.70, 0], [0, 4.5, 8], [0, 0, 2000]),
    FlightData(2500, 98500, 283.0, [0, 13.10, 0], [0, 5, 9], [0, 0, 2500]),
    FlightData(2700, 98200, 282.5, [0, 13.30, 0], [0, 5.2, 9.5], [0, 0, 2700]),
    FlightData(2800, 98000, 282.3, [0, 13.40, 0], [0, 5.3, 9.7], [0, 0, 2800]),
    FlightData(2850, 97800, 282.1, [0, 13.50, 0], [0, 5.4, 9.8], [0, 0, 2850]),
    FlightData(2900, 97600, 281.9, [0, 13.60, 0], [0, 5.5, 9.9], [0, 0, 2900]),
    FlightData(2950, 97400, 281.7, [0, 13.70, 0], [0, 5.6, 9.95], [0, 0, 2950]),
    FlightData(2975, 97300, 281.6, [0, 13.80, 0], [0, 5.7, 9.98], [0, 0, 2975]),
    FlightData(2990, 97200, 281.5, [0, 13.90, 0], [0, 5.8, 9.99], [0, 0, 2990]),
    FlightData(2995, 97150, 281.4, [0, 13.95, 0], [0, 5.9, 9.995], [0, 0, 2995]),
    FlightData(3000, 97100, 281.3, [0, 14.00, 0], [0, 6, 10], [0, 0, 3000]),
    # Descend simulation
    FlightData(2995, 97150, 281.4, [0, calculate_gravity(0), 0], [0, 5.9, 9.995], [0, 0, 2995]),
    FlightData(2990, 97200, 281.5, [0, calculate_gravity(0), 0], [0, 5.8, 9.99], [0, 0, 2990]),
    FlightData(2975, 97300, 281.6, [0, calculate_gravity(0), 0], [0, 5.7, 9.98], [0, 0, 2975]),
    FlightData(2950, 97400, 281.7, [0, calculate_gravity(0), 0], [0, 5.6, 9.95], [0, 0, 2950])
]
