from sense_hat import SenseHat
from publisher import Publisher


joondalup = Publisher()

while True:
    joondalup.get_running_total()
    joondalup.get_time()
    joondalup.get_temperature()
    data = joondalup.get_update()
    joondalup.publish(data)
