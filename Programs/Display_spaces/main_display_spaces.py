from subscriber import Subscriber


update = Subscriber()
update.mqtt_connect()

while True:
    update.display()
