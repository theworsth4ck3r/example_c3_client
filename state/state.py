class State:

	def __init__(self):
		self.state = {}

	def getState(self):
		return self.state

	def setState(self, key, value):
		self.state[key] = value

	def getFromState(self, key):
		return self.state[key]