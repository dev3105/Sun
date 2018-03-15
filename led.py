#! /usr/bin/env python
import Rpi.GPIO as GPIOimport time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

GPIO.output(7,True)