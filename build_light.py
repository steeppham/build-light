import sys
import schedule
import time
from DelcomPython import DelcomUSBDevice

PERIOD = 10

def flash():
  print("hello world")

def initialise_light():
  delcom = DelcomUSBDevice()
  if delcom.find() == 0:
    print("failed to find device")
    sys.exit(0)
  delcom.open()
  print("device found:", delcom.DisplayInfo())
  return delcom

schedule.every(PERIOD).seconds.do(flash)
initialise_light()
while True:
  schedule.run_pending()
  time.sleep(1)
