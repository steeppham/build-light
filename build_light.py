from __future__ import print_function
import sys
import schedule
import time
from DelcomPython import DelcomUSBDevice

PERIOD = 10

def flash():
  print("Hello World")
  delcom.LEDControl(delcom.LED1, delcom.LEDON)

def initialise_delcom():
  delcom = DelcomUSBDevice()
  if delcom.find() == 0:
    print("Failed to find delcom device")
    sys.exit(0)
  delcom.open()
  print("Delcom device found.")
  delcom.DisplayInfo()
  return delcom

schedule.every(PERIOD).seconds.do(flash)
delcom = initialise_delcom()

while True:
  try:
    schedule.run_pending()
    time.sleep(1)
  except KeyboardInterrupt:
    delcom.LEDControl(delcom.LEDALL, LEDOFF)
    delcom.close()
    print("Terminating")
    sys.exit(0)
