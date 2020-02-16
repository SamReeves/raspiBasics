#!/usr/bin/env python3

from time import sleep
from gpiozero import LED, Button, Buzzer
from picamera import PiCamera
from datetime import datetime
import Adafruit_GPIO
import Adafruit_SSD1306

buzzer = Buzzer(18)
led1 = LED(19)
led2 = LED(20)
led3 = LED(21)
button = Button(16)
camera = PiCamera()

def countDown():
    camera.start_preview()
    led1.on()
    sleep(1)
    led2.on()
    sleep(1)
    led3.on()
    sleep(1)
    buzzer.on()
    led1.off()
    led2.off()
    led3.off()
    sleep(1)
    buzzer.off()
    takeSelfie()

def takeSelfie():
    timestamp = datetime.now().isoformat()
    camera.capture(str(timestamp) + '.jpg')
    camera.stop_preview()

while True:
    button.when_pressed = countDown
