#!/usr/bin/python

# Copyright 2014 Medando UG (haftungsbeschraenkt)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# http://medando.de


import paho.mqtt.client as mqtt

MQTT_BROKER_HOSTNAME = 'test.mosquitto.org'
MQTT_TOPIC = 'de/medando/#'


def on_message(client, userdata, message):
    print("%s %s" % (message.topic, str(message.payload)))


if __name__ == "__main__":
    mqtt_client = mqtt.Client()
    mqtt_client.on_message = on_message

    mqtt_client.connect(MQTT_BROKER_HOSTNAME, 1883, 60)
    mqtt_client.subscribe(MQTT_TOPIC, 0)

    mqtt_client.loop_forever()
