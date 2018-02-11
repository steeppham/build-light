import requests
import pytest
from build import BuildStatus

@pytest.fixture
def mock_pass_request(mocker):
  mock_request = mocker.patch.object(requests, 'get', autospec=True)
  mock_response = mocker.Mock()
  mock_response.text = "PASS"
  mock_request.return_value = mock_response
  return mock_request

def test_should_request_with_url(mock_pass_request):
  build_status = BuildStatus('example.com/cctray.xml')
  status = build_status.check()
  mock_pass_request.assert_called_once_with('example.com/cctray.xml')

def test_should_respond_with_pass(mock_pass_request):
  build_status = BuildStatus('example.com/cctray.xml')
  status = build_status.check()
  assert status == "PASS"
