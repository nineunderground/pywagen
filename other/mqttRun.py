# @Author: Iñaki Rodriguez <inaki>
# @Date:   14-May-2018
# @Project: pywagen
# @Filename: mqttRun.py
# @Last modified by:   inaki
# @Last modified time: 14-May-2018
##################
# MQTT example   #
##################

from lib.mqtt import MQTTClient
from network import WLAN
import machine
import time
import pycom
from ubinascii import hexlify

pycom.heartbeat(False)

led_topic = "irodri/feeds/RGB LED"


def sub_cb(topic, msg):
    if topic.decode("utf-8") == led_topic:
        msgDecoded = msg.decode("utf-8")
        if(msgDecoded == 'OFF'):
            pycom.rgbled(0xFF0000)  # RED
        if(msgDecoded == 'ON'):
            pycom.rgbled(0x00FF00)  # GREEN


wlan = WLAN(mode=WLAN.STA)
nets = wlan.scan()
for net in nets:
    if net.ssid == 'Iphoneto7':
        wlan.connect(net.ssid, auth=(net.sec, '12121212'), timeout=5000)
        while not wlan.isconnected():
            machine.idle()  # save power while waiting
        print('WLAN connection succeeded!')
        break

client = MQTTClient("wipy2", "io.adafruit.com", user="irodri",
                    password="c9cbd8917446484d9f01d7547938c78c", port=1883)

client.set_callback(sub_cb)
client.connect()
client.subscribe(topic=led_topic)
# client.publish(topic=led_topic, msg="OFF")


pycom.rgbled(0xFF0000)  # RED
while True:
    client.check_msg()
