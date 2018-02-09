import ConfigParser

class Config:
  def __init__(self, file):
    self.config = ConfigParser.ConfigParser()
    self.config.read(file)

  def get_feed_url(self):
    return self.config.get('build', 'feed_url')
