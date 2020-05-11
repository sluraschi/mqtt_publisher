# MQTT Publish Demo

import time

from mqtt_client import MqttClient
from helpers import split_by_size


def publish(file_path):
    client = MqttClient("tailor.cloudmqtt.com", "ysdkltdu", "5SX1fOJNL4en")

    start = time.time()
    list_of_payloads = split_by_size(file_path)
    success = client.send_multiple_messages(list_of_payloads)
    end = time.time()

    if success:
        mssg = '\nAll segments sent!'
    else:
        mssg = '\nAn error was found while publishing'
    elapsed = end - start
    print(mssg)
    print('Elapsed time:', elapsed, 'seconds')


if __name__ == "__main__":
    file = "paquete_vacio"
    publish(file)
