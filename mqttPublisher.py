# MQTT Publish Demo

import paho.mqtt.publish as publish
from itertools import islice
import time

SEGMENT_LINES = 13
HEADER_LINES = 3
TOPIC = "/pi/test"


# for testing purpose
def send_single_message(file):
    print 'Sending single message...'
    payload = get_next_segment(file)
    if payload == '':
        return False
#            publish.single(topic="topic/state", payload = payload, hostname="192.168.1.110")
    publish.single(topic=TOPIC, payload=payload, qos=1, hostname="tailor.cloudmqtt.com", port=18096,
                   auth={'username': 'ysdkltdu', 'password': '5SX1fOJNL4en'})
    return True


def get_next_segment(file):
    lines = [x.strip() for x in islice(file, SEGMENT_LINES)]
    return '\n'.join(lines)


def get_all_segments(file):
    segments = list()
    while True:
        next_seg = get_next_segment(file)
        if not next_seg:
            break
        segments.append(next_seg)
    return segments


def send_file_header(file):
    lines = [x.strip() for x in islice(file, HEADER_LINES)]
    header = '\n'.join(lines)
#    publish.single(topic="topic/state", payload=payload, hostname="192.168.1.110")
    publish.single(topic=TOPIC, payload=header, qos=1, hostname="tailor.cloudmqtt.com", port=18096,
                   auth={'username': 'ysdkltdu', 'password': '5SX1fOJNL4en'})


# Using publish.multiple keeps the connection alive
def send_multiple_messages(file):
    print 'Sending multiple message...'
    segments = get_all_segments(file)
    payloads = list()
    for seg in segments:
        payloads.append([TOPIC, seg, 1, False])
#    publish.multiple(payloads, hostname="192.168.1.110")
    publish.multiple(payloads, hostname="tailor.cloudmqtt.com", port=18096,
                     auth={'username': 'ysdkltdu', 'password': '5SX1fOJNL4en'})


def main():
    file_path = 'paquete_ejemplo'

    start = time.time()
    with open(file_path, 'r') as file:
        send_file_header(file)
        print 'Header of the file sent!'
        send_multiple_messages(file)
        print 'All segments sent!'
    end = time.time()
    elapsed = end - start
    print 'Elapsed time:', elapsed, 'seconds'


if __name__ == "__main__":
    main()
