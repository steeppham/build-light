from __future__ import print_function
import sys
import schedule
import time
from DelcomPython import DelcomUSBDevice
from light import Light

PERIOD = 10

def flash():
  print("Hello World")
  light.green()

schedule.every(PERIOD).seconds.do(flash)
light = Light()
light.reset()

while True:
  try:
    schedule.run_pending()
    time.sleep(1)
  except KeyboardInterrupt:
    light.close()
    print("Terminating")
    sys.exit(0)
