from Programs.Count_cars.publisher import Publisher
import json


class Subscriber(Publisher):
    """This class subscribes to the Publisher's updates and shows the number of available parking spots
    on a display together with temperature and time of the reading."""

    def __init__(self, update_received=None, available_spaces_received=None, time_received=None,
                 temperature_received=None):
        super().__init__()

        self.update_received = update_received
        self.available_spaces_received = available_spaces_received
        self.time_received = time_received
        self.temperature_received = temperature_received

    def on_connect(self, client, userdata, flags, rc):
        """Callback function called in response to being successfully connected to the client.
        Also, it subscribes to the topic."""

        client.subscribe(self.TOPIC)
        return "Connected with result code " + str(rc)

    def on_message(self, client, userdata, message):
        """Retrieves updates from the topic 'Joondalup City Square Parking' and converts the messages back into
        dictionary."""

        self.update_received = json.loads(message.payload.decode("utf-8"))
        return self.update_received

    def mqtt_connect(self):
        """Subscribes to carpark updates sent by the Publisher to topic 'Joondalup City Square Parking'."""

        client = self.CLIENT
        client.connect(self.BROKER_HOST, self.BROKER_PORT)
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.loop_forever()

    def display(self):
        """Shows time, temperature and available number of spaces on the Raspberry Pi's display.
        The initial display starts with: ---
        If there are no spaces available, the displays shows: FULL
        Negative number of spaces are not allowed.
        """

        WHITE = (255, 255, 255)
        BLUE = (0, 0, 255)

        self.available_spaces_received = self.update_received['AVAILABLE SPACES']
        self.time_received = self.update_received['TIME']
        self.temperature_received = self.update_received['TEMPERATURE']

        # initial default display: ---
        if self.available_spaces_received is None:
            self.sense.show_message(text_string='---', scroll_speed=0.1, text_colour=BLUE, back_colour=WHITE)

        else:
            self.sense.show_message(text_string=self.time_received, scroll_speed=0.1, text_colour=BLUE,
                                    back_colour=WHITE)
            self.sense.show_message(text_string=self.temperature_received, scroll_speed=0.1, text_colour=BLUE,
                                    back_colour=WHITE)

            # carpark full
            if self.available_spaces_received <= 0:
                self.sense.show_message(text_string='FULL', scroll_speed=0.1, text_colour=BLUE, back_colour=WHITE)

            # carpark emtpy
            elif self.available_spaces_received >= self.TOTAL_SPACES:
                self.sense.show_message(text_string=str(self.TOTAL_SPACES), scroll_speed=0.1, text_colour=BLUE,
                                        back_colour=WHITE)

            # carpark's available spaces
            else:
                self.sense.show_message(text_string=str(self.available_spaces_received), scroll_speed=0.1,
                                        text_colour=BLUE, back_colour=WHITE)
