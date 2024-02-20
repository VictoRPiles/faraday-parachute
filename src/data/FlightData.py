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
    FlightData(100, 100, 100,
               [100, 100, 100],
               [100, 100, 100],
               [100, 100, 100]),
    FlightData(90, 100, 100,
               [100, calculate_gravity(90), 100],
               [100, 100, 100],
               [100, 100, 100])
]
