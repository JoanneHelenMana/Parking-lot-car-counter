from sense_hat import SenseHat
from Programs.Configuration.configuration import Configuration
from datetime import datetime


class Carpark:
    """This class creates a carpark where a running total of available spaces is provided
    at any given moment, together with temperature and time information of the reading."""

    INITIAL_AVAILABLE_SPACES = int(Configuration.from_file()['available-spaces'])
    TOTAL_SPACES = int(Configuration.from_file()['number-of-spaces'])
    LOCATION = str(Configuration.from_file()['location'])

    def __init__(self, available_spaces=None, time=None, temperature=None):
        self.sense = SenseHat()

        self.available_spaces = available_spaces
        self.time = time
        self.temperature = temperature

    def get_running_total(self):
        """Keeps a running total of cars by adding and subtracting entering and exiting cars
        from a given initial available number of spaces."""

        self.available_spaces = self.INITIAL_AVAILABLE_SPACES

        while True:
            for event in self.sense.stick.get_events():
                if event.action == "pressed":

                    # up: car enters
                    if event.direction == "up":
                        self.available_spaces = self.INITIAL_AVAILABLE_SPACES - 1
                        self.INITIAL_AVAILABLE_SPACES = self.available_spaces

                    # down: car exits
                    elif event.direction == "down":
                        self.available_spaces = self.INITIAL_AVAILABLE_SPACES + 1
                        self.INITIAL_AVAILABLE_SPACES = self.available_spaces

                    return self.available_spaces

    def get_time(self):
        """Gets the current time in the format 'HH:MM'."""

        self.time = datetime.now().strftime("%H:%M")

        return self.time

    def get_temperature(self):
        """Gets the current temperature in Celsius degrees from the SenseHat sensor."""

        self.temperature = self.sense.get_temperature()
        self.temperature = float("{:.1f}".format(self.temperature))

        return self.temperature
