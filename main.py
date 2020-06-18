# main.py -- put your code here!
import pycom
from network import WLAN
import machine
from machine import Pin
from mqtt import MQTTClient
import time

def settimeout(duration):
    pass



wlan = WLAN(mode=WLAN.STA)
wlan.connect("AnBrEiJo", auth=(WLAN.WPA2, "Detergratis1"), timeout=5000)

while not wlan.isconnected():

     machine.idle()

client = MQTTClient("device_id", "broker.hivemq.com", port=1883)
client.connect()

print("Client connected")

adc = machine.ADC()
apin = adc.channel(pin="P16")
led_red = Pin("P8", mode=Pin.OUT)
led_green = Pin("P9", mode=Pin.OUT)

while True:
    millivolts = apin.voltage()
    degC = (millivolts - 500.0) / 10
    degF = ((degC * 9.0) / 5.0) + 32

    client.publish("a/b/c/pycomdevice", str(degC))
    pybytes.send_signal(1, degC)

    print(millivolts)
    print(degC)
    print(degF)

    if degC >= 29.0:
        for x in range(5):
            led_red.value(1)
            time.sleep(1)
            led_red.value(0)
            time.sleep(1)
    else:
        for x in range(5):
            led_green.value(1)
            time.sleep(1)
            led_green.value(0)
            time.sleep(1)
