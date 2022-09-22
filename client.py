import socketio
from module_radar import ModuleDistanceDetector
import time

sio = socketio.Client()
distanceDetector = ModuleDistanceDetector()

@sio.event
def connect():
    print("I'm connected!")

@sio.event
def connect_error(data):
    print("The connection failed!")

@sio.event
def disconnect():
    print("I'm disconnected!")
    #distanceDetector.close()
    #distanceDetector = None

sio.connect('http://127.0.0.1:5055')



distanceDetector.start()
start = time.monotonic()
duration = 120 # Seconds

while time.monotonic() - start < duration:
    distance = distanceDetector.read()
    time.sleep(0.3)
    print("\nDistance: ",distance)
    sio.emit('radarDistance', {"distance": distance})

#for i in range(100):
#    distance = distanceDetector.read()
#    time.sleep(0.3)
#    print("\nDistance: ",distance)
#    sio.emit('radarDistance', {"distance": distance})

distanceDetector.close()
sio.disconnect()