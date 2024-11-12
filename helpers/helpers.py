import queue
import datetime
import requests

def getPublicIp():
    response = requests.get('https://api.ipify.org?format=json')    
    return response.json().get('ip')


def getFileContents(filePath):
	_file = open(filePath)
	_contents = _file.read()
	_contents = _contents.strip()
	_file.close()
	
	return _contents


def makeQueue(arrayOfSomething):
	_Q = queue.Queue()

	for x in range(0, len(arrayOfSomething)):
		_Q.put(arrayOfSomething[x])

	return _Q


def getCurrentDateTime():
	now = datetime.datetime.now()

	_month = str(now.month)
	_day = str(now.day)

	_hours = str(now.hour)
	_minutes = str(now.minute)
	_seconds = str(now.second)

	if now.month < 10:
		_month = '0' + _month

	if now.day < 10:
		_day = '0' + _day

	if now.hour < 10:
		_hours = '0' + _hours

	if now.minute < 10:
		_minutes = '0' + _minutes

	if now.second < 10:
		_seconds = '0' + _seconds


	_d = '%d_%s_%s' % (now.year, _month, _day)
	_t = '%s_%s_%s' % (_hours, _minutes, _seconds)

	return '[%s_%s]' % (_d, _t)