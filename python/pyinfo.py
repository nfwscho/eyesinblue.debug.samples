import os
import sys

# print full path of the currently running Python
print("Currently running python : " + sys.executable)

# print PYTHONPATH
print("-- PYTHONPATH -- ")
try:
	user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
	print('\n'.join(user_paths))
except:
	print("There's no PYTHONPATH")
	user_paths = []


print("-- sys.paths -- ")
try:
	print('\n'.join(sys.paths))
except:
	print("There's no sys.path")
	user_paths = []

