import serial_comm
import mqtt_publisher
import os
from datetime import datetime


if __name__ == "__main__":
    while 1:
        print("Starting serial comm...")
        file_name = serial_comm.read_sensor()
        print("OK!")
        print("Starting to publish file:", file_name, "...")
        mqtt_publisher.publish(file_name)
        print("OK!")


