#!/usr/bin/env python3
from time import sleep
from gpiozero import LED, Button

button = Button(16)

led1 = LED(19)
led2 = LED(20)
led3 = LED(21)

on_or_off = False


def LEDdance():
    led1.on()
    sleep(0.5)
    led1.off()
    led2.on()
    sleep(0.5)
    led2.off()
    led3.on()
    sleep(0.5)
    led3.off()

def toggle():
    global on_or_off
    on_or_off = not on_or_off


while True:
    button.when_pressed = toggle
    while on_or_off == True:
        LEDdance()

