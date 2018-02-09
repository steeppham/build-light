from __future__ import print_function
import sys
import schedule
import time
from DelcomPython import DelcomUSBDevice

PERIOD = 10

def flash():
  print("Hello World")

def initialise_light():
  delcom = DelcomUSBDevice()
  if delcom.find() == 0:
    print("Failed to find delcom device")
    sys.exit(0)
  delcom.open()
  print("Delcom device found:", delcom.DisplayInfo())
  return delcom

schedule.every(PERIOD).seconds.do(flash)
initialise_light()
while True:
  schedule.run_pending()
  time.sleep(1)
