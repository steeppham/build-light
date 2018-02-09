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
    self.delcom.LEDControl(self.delcom.LEDALL, self.delcom.LEDOFF)

  def green(self):
    self.delcom.LEDControl(self.delcom.LED1, self.delcom.LEDON)
