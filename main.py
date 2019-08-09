########################################
# @Author: Iñaki Rodriguez <inaki>
# @Date:   06-May-2018
# @Filename: main.py
# @Last modified by:   inaki
# @Last modified time: 17-May-2018
########################################
import pycom

pycom.heartbeat(False)

"""
Test Car admin panel
--------------------

It is a BLE broadcasting microcontroller that manages the common tasks
related to a vehicle

- 1. Shows the status of car doors
- 2. It receives the bluetooth cmds to open/close all doors
- 3. It receives the bluetooth cmds to open/close back door throw proximity sensor

"""

# Broadcasting BLE and stablish connection
from network import Bluetooth
import time
import machine

bluetooth = Bluetooth()
bluetooth.set_advertisement(
    name='PyWagenHub', manufacturer_data='manufacturer data', service_uuid=b'1234567890123456')

service = bluetooth.service(b'1234567890123457', isprimary=True, nbr_chars=1, start=True)


def conn_cb(bt_o):
    events = bt_o.events()   # This method returns the flags and clears the internal registry
    print(events)
    if events & Bluetooth.CLIENT_CONNECTED:
        print("Client connected")
    elif events & Bluetooth.CLIENT_DISCONNECTED:
        print("Client disconnected")


bluetooth.callback(trigger=Bluetooth.CLIENT_CONNECTED |
                   Bluetooth.CLIENT_DISCONNECTED, handler=conn_cb)
bluetooth.advertise(True)

while True:
    print('Print info:')
    print('TASK - Car doors status')
    print('***********************')
    print('Left front door' + str(car.lf_door.isOpen()))
    print('Right front door' + str(car.rf_door.isOpen()))
    print('Left back door' + str(car.lb_door.isOpen()))
    print('Left back door' + str(car.rb_door.isOpen()))

    time.sleep(2.5)
    # machine.idle()
