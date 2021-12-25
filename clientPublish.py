import paho.mqtt.client as mqtt
import time
from sense_hat import SenseHat
sense = SenseHat()

# Setting mqtt client

client = mqtt.Client("python_pub")

#setting up mqtt username and pw
client.username_pw_set(username="pi", password ="omaromar")

#setting getaway server to publish to
client.connect("127.0.0.1",1883)
client.loop_start()
try:
    while True:
        client.publish("sense/temp", round(sense.get_temperature(),2))
        client.publish("sense/humid", round(sense.get_humidity(),2))
        client.publish("sense/pressure",round(sense.get_pressure(),2))
        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']
        x=round(x,2)
        y=round(y,2)
        z=round(z,2)
        stro="%d, %d, %d " %(x,y,z)
        client.publish("sense/accel", stro)
        time.sleep(10)
except KeyboardInterrupt:
    print("interrupted")
client.loop_stop()
        
        