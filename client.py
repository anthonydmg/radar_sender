import socketio
from module_radar import ModuleDistanceDetector
import time

sio = socketio.Client()

@sio.event
def connect():
    print("I'm connected!")

@sio.event
def connect_error(data):
    print("The connection failed!")

@sio.event
def disconnect():
    print("I'm disconnected!")

sio.connect('http://127.0.0.1:5055')


distanceDetector = ModuleDistanceDetector()
distanceDetector.start()

for i in range(20):
    distance = distanceDetector.read()
    time.sleep(0.2)
    print("Distance: ",distance)
    sio.emit('radarDistance', {"distance": distance})

distanceDetector.close()
sio.disconnect()