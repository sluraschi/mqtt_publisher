import serial_comm
import mqtt_publisher
import os
from datetime import datetime


if __name__ == "__main__":
    file_name = serial_comm.read_sensor()
    mqtt_publisher.publish(file_name)

    now = datetime.now()
    dt_string = now.strftime("%d_%m_%Y-%H%M%S")

    os.rename(file_name, "/home/pi/package-storage/" + "[" + dt_string + "]-" + file_name)
#    os.rename(file_name, "/Users/sebastianluraschi/Documents/Repositories/TP_prof/Mqtt_publisher" + "[" + dt_string + "]-" + file_name)
