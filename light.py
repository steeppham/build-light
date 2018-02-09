from DelcomPython import DelcomUSBDevice

class Light:

  def __init__(self):
    self.delcom = DelcomUSBDevice()
    if self.delcom.find() == 0:
      raise Exception("Delcom device not found")
    self.delcom.open()
    print("Delcom device found.")
    self.delcom.DisplayInfo()

  def close(self):
    self.reset()
    self.delcom.close()

  def reset(self):
    self.delcom.LEDControl(delcom.LEDALL, delcom.LEDOFF)

  def green(self):
    self.delcom.LEDControl(delcom.LED1, delcom.LEDON)
