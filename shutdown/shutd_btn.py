#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#   RPi-CM3MB2/MB3 Shutdown Button handler
#   "shutd_btn.py"
#   2018/03/13 R1.0
#   RATOC Systems, Inc. Osaka, Japan
#
import RPi.GPIO as GPIO
import os, time

shutd_ctl = 6     #GPIO 06 for Shutdown Control

GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
GPIO.setup(shutd_ctl, GPIO.IN, pull_up_down=GPIO.PUD_UP)
print( "RPi-CM3MBx Shutdown Button handler" )

def isr_shutdown(self):
    print( "Shutdown Button is activated !!" )
    os.system( "sudo shutdown -h now" )

GPIO.add_event_detect(shutd_ctl, GPIO.FALLING, callback=isr_shutdown, bouncetime=2000)

while(True):
    time.sleep(1)

GPIO.cleanup()

