import serial_comm
import mqtt_publisher
import os
from datetime import datetime


if __name__ == "__main__":
    print("Starting serial comm...", end="")
    file_name = serial_comm.read_sensor()
    print("OK!")
    print("Starting to publish file:", file_name, "...", end="")
    mqtt_publisher.publish(file_name)
    print("OK!")
    now = datetime.now()
    dt_string = now.strftime("%d_%m_%Y-%H%M%S")
    print("Moving file...", end="")
    os.rename(file_name, "/home/pi/package-storage/" + "[" + dt_string + "]-" + file_name)
#    os.rename(file_name, "/Users/sebastianluraschi/Documents/Repositories/TP_prof/Mqtt_publisher" + "[" + dt_string + "]-" + file_name)
    print("OK!")
