from config import Config

def test_should_read_feed_url_from_config():
  config = Config('config.sample.ini')
  url = config.get_feed_url()
  assert url == "https://circleci.com/cc.xml?circle-token=:circle-token"
