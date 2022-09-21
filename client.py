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
    distanceDetector.close()
    distanceDetector = None

sio.connect('http://127.0.0.1:5055')


#distanceDetector = ModuleDistanceDetector()
distanceDetector.start()

for i in range(100):
    distance = distanceDetector.read()
    time.sleep(0.3)
    print("Distance: ",distance)
    sio.emit('radarDistance', {"distance": distance})

distanceDetector.close()
sio.disconnect()