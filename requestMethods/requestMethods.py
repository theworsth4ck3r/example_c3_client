import urllib.request as request
import http.cookiejar


def getOpener():
	jar = http.cookiejar.FileCookieJar('cookies')

	_opener = request.build_opener(request.HTTPCookieProcessor(jar))
	_opener.addheaders = [
		('User-agent', 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT 4.0)'),
		('X-Requested-With', 'XMLHttpRequest')
	]

	return _opener


def sendRequest(url, data = None, files = None):

	_opener = getOpener()

	try:
		_opener.open(url)
		_response = _opener.open(url, data)
		return _response.read().decode('utf-8')
	except Exception as e:
		# raise e
		print("Request error!")
		return False