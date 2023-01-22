"""
Python script that converts CAN messages into MQTT messages and back
"""

import can
import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    """
    Callback for when the client successfully connects to the broker
    """
    print("Connected with result code "+str(rc))
    client.subscribe("can")

def on_message(client, userdata, msg):
    """
    Callback for when a message is received
    """
    print(msg.topic+" "+str(msg.payload))
    bus.send(create_frame(msg.payload))

def create_frame(data):
    """
    Creates a CAN frame from an MQTT message
    """
    frame_data = data.split(",")
    return can.Message(arbitration_id=int(frame_data[0]), data=[int(x) for x in frame_data[1:]])

def create_message(frame):
    """
    Creates an MQTT message from a CAN frame
    """
    return str(frame.arbitration_id)+","+",".join([str(x) for x in frame.data])

def main():
    """
    Main loop of the program
    """
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("iot.eclipse.org", 1883, 60)
    client.loop_start()
    
    while True:
        frame = bus.recv()
        if frame:
            client.publish("can", create_message(frame))
        time.sleep(0.1)

if __name__ == "__main__":
    client = mqtt.Client()
    bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=250000)
    main()