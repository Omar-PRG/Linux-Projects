import paho.mqtt.client as mqtt
from sense_hat import SenseHat
sense = SenseHat()
X=[255,0,0]
O=[255,255,255]
# Setting mqtt client
def on_connect(client,userdata,flags,rc):
    print("connected with result code"+str(rc))
    client.subscribe("textbox")


def on_message(client,userdata,msg):
    print("got the following message %s " %(msg.payload))
    
 
    image=[O, O, O, X, X, O, O, O,O,O,X,O,O,X,O,O,O,O,O,O,O,X,O,O,O,O,O,O,X,O,O,O,O,O,O,X,O,O,O,O,O,O,O,X,O,O,O,O,O,O,O,X,O,O,O,O,O,O,O,X,O,O,O,O]
    data=msg.payload   #is an pbject
    x=data.decode("utf-8")
    print(x)         #is a string
    def Convert(string):
        list1=[]
        list1[:0] = string
        return list1
    nist=Convert(x)   #nist is a list
    print(nist)
    final=nist.replace("'","")
    sense.set_pixels(final)
    
    
    
client=mqtt.Client()
client.username_pw_set(username="pi", password ="omaromar")

client.on_connect = on_connect

client.on_message = on_message

client.connect("127.0.0.1",1883,60)
try:

    client.loop_forever()
        
except KeyboardInterrupt:
    print("interrupted")