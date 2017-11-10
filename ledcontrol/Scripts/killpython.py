import os
import signal
import sys

ID = sys.argv[1]

os.kill(int(ID), signal.SIGKILL)
