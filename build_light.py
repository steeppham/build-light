import schedule
import time

PERIOD = 10

def flash():
  print("hello world")

schedule.every(PERIOD).seconds.do(flash)

while True:
  schedule.run_pending()
  time.sleep(1)
