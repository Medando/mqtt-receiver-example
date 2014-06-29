Medando MQTT Example
====================

Example application for receiving Quantified Self data via MQTT.

These Python scrips demonstrate how to receive data from [Medando](http://medando.de) apps. The Android apps
[BloodPressureCompanion](https://play.google.com/store/apps/details?id=de.medando.bloodpressurecompanion)
and [WeightCompanion](https://play.google.com/store/apps/details?id=de.medando.weightcompanion)
have *experimental* support for sending the latest entries as MQTT messages.

Read more about the MQ Telemetry Transport (MQTT) protocol at [MQTT.org](http://mqtt.org).


Installation of requirements
----------------------------

Install Python as described on [python.org](https://www.python.org/) (if it's not installed on
your system already). We recommend to install the Python distribution
[Anaconda](https://store.continuum.io/cshop/anaconda/).


Install the Paho MQTT client library for Python (https://pypi.python.org/pypi/paho-mqtt):

```sh
pip install -r requirements.txt
```

Configure the MQTT Broker
-------------------------

Within the scripts configure the host name of the MQTT broker that you use.
You must use the same MQTT broker that you configured in the Android apps.

![WeightCompanion MQTT settings](https://raw.githubusercontent.com/Medando/mqtt-example/master/images/screenshot_weightcompanion_settings_mqtt.png)

test.mosquitto.org is an public test server that you can use for testing.

```python
MQTT_BROKER_HOSTNAME = 'test.mosquitto.org'
```

We recommend to setup your own MQTT broker which should be non-public and secured.

Starting the example
--------------------

To receive your MQTT messages start the simple MQTT subscriber:

```sh
python mqtt-subscriber.py
```

After you configured MQTT in the Android app, you should see something like:

```
de/medando/weightcompanion {"unit":"kg","weight":73.1}
```

This very simple example runs as an infinite loop. To end execution, use Ctrl-C.

Continue...
-----------

Continue from here with more serious examples and applications.
For example, evaluate the received MQTT *payload* with your data by extending the Python script.

You should also change the MQTT *topic* to something more specific than the default topic.

```python
MQTT_TOPIC = 'de/medando/#'
```

