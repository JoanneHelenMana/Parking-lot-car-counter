from carpark import Carpark
from Programs.Configuration.configuration import Configuration
import paho.mqtt.client as mqtt
import json


class Publisher(Carpark):
    """Every time a car enters or exits the carpark, this class publishes an update to an MQTT server
    containing the number of available spaces together with the temperature and time of the reading."""

    BROKER_HOST = str(Configuration.from_file()['broker-host'])
    BROKER_PORT = int(Configuration.from_file()['broker-port'])
    TOPIC = str(Configuration.from_file()['location'])
    CLIENT = mqtt.Client()

    def __init__(self, update=None, json_update=None):
        super().__init__()

        self.update = update
        self.json_update = json_update

    def get_update(self):
        """Retrieves the information provided by the carpark -available spaces, time, and temperature-
        and formats it into a dictionary."""

        self.update = dict()
        self.update['AVAILABLE SPACES'] = self.available_spaces
        self.update['TIME'] = self.time
        self.update['TEMPERATURE'] = self.temperature

        return self.update

    def publish(self, data):
        """Connects and publishes updates to the MQTT server."""

        self.json_update = json.dumps(data)

        client = self.CLIENT
        client.connect(host=self.BROKER_HOST, port=self.BROKER_PORT)
        client.publish(topic=self.TOPIC, payload=self.json_update)
