import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

class HTTPGetReq:
  def __init__(self, _getURL='', _getParams='', _headerDict={}, _connectTimeOut=25, _readTimeOut=25, _retries=3):
    self.getURL = _getURL
    self.getParams = _getParams
    self.headerDict = _headerDict
    self.connectTimeOut = int(_connectTimeOut)
    self.readTimeOut = int(_readTimeOut)
    self.retries = int(_retries)

  def GetHTTPReqStatus(self):
    retHTTPStatus = -1
    try:
      httpSession = requests.Session()
      httpSession.mount(self.getURL, HTTPAdapter(max_retries=self.retries))
      response = httpSession.get(self.getURL, params = self.getParams, headers=self.headerDict, timeout=(self.connectTimeOut, self.readTimeOut))
      retHTTPStatus = response.status_code
      httpSession.close()
    except Exception as excepErr:
      print("Request URL :{}: -> Response Code ::".format(self.getURL))
      print("Exception in Making HTTP Get Request :{}: -> :{}:".format(self.getURL, excepErr))
      pass
    return retHTTPStatus

def main():
  try:
    for i in range (1,10):
      serviceURL = "http://whythishappens.com/"
      print(serviceURL)
      httpReq = HTTPGetReq(_getURL = serviceURL, _connectTimeOut=5, _readTimeOut=5, _retries=3)
      httpReq.GetHTTPReqStatus()
  except Exception as excepErr:
    print("Exception in main() -> :{}:".format(excepErr))

if __name__ == '__main__':
  main()
