import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import time

HEADER_LINES = 3
TOPIC = "/pi/test"


class MqttClient:
    def __init__(self, host, usr, password):
        self.client = mqtt.Client(protocol=mqtt.MQTTv311)
        self.client.on_publish = MqttClient.on_publish
        self.client.username_pw_set("ysdkltdu", "5SX1fOJNL4en")
        self.client.connect("tailor.cloudmqtt.com", port=18096, keepalive=60)
        self.client.loop_start()

    def __del__(self):
        self.client.loop_stop()

    @staticmethod
    def on_publish(client, userdata, mid):
        print 'Published message with id:', mid

    def send_multiple_messages(self, segments):
        print '\nSending multiple payloads...'
        success_status = True
        for seg in segments:
            result = self.client.publish(topic=TOPIC, payload=seg, qos=1)
            time.sleep(2)
            result.wait_for_publish()
            if result.rc != 0:
                print 'Error publishing in message', result.mid, 'with code:', result.rc
                success_status = False
        return success_status

# for testing purpose
# def send_single_message(file):
#     print 'Sending single message...'
#     payload = get_next_segment(file)
#     if payload == '':
#         return False
#     publish.single(topic="topic/state", payload = payload, hostname="192.168.1.110")
#     publish.single(topic=TOPIC, payload=payload, qos=1, hostname="tailor.cloudmqtt.com", port=18096,
#                    auth={'username': 'ysdkltdu', 'password': '5SX1fOJNL4en'})
#     return True


# def send_file_header(file):
#     lines = [x.strip() for x in islice(file, HEADER_LINES)]
#     header = '\n'.join(lines)
#     publish.single(topic="topic/state", payload=payload, hostname="192.168.1.110")
#     publish.single(topic=TOPIC, payload=header, qos=1, hostname="tailor.cloudmqtt.com", port=18096,
#                    auth={'username': 'ysdkltdu', 'password': '5SX1fOJNL4en'})