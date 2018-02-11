import requests

class BuildStatus:
  def __init__(self, url):
    self.url = url

  def check(self):
    r = requests.get(self.url)
    return r.text
