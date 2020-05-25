import os
import sys
import sys
import shutil
import pkgutil
import importlib
import collections


if sys.version_info.major == 2:
	raise NotImplementedError('CPython 2 is not supported yet')


def main():

	print("-- loaded module -- ")
	print('\n'.join(sys.modules))

	print("-- installed module -- ")
#	print(help("modules"))

	# name this file (module)
	this_module_name = os.path.basename(__file__).rsplit('.')[0]

	# dict for loaders with their modules
	loaders = collections.OrderedDict()

	# names`s of build-in modules
	for module_name in sys.builtin_module_names:

		# find an information about a module by name
		module = importlib.util.find_spec(module_name)

		# add a key about a loader in the dict, if not exists yet
		if module.loader not in loaders:
			loaders[module.loader] = []

		# add a name and a location about imported module in the dict
		loaders[module.loader].append((module.name, module.origin))

	# all available non-build-in modules
	for module_name in pkgutil.iter_modules():

		# ignore this module
		if this_module_name == module_name[1]:
			continue

		# find an information about a module by name
		module = importlib.util.find_spec(module_name[1])

		# add a key about a loader in the dict, if not exists yet
		loader = type(module.loader)
		if loader not in loaders:
			loaders[loader] = []

		# add a name and a location about imported module in the dict
		loaders[loader].append((module.name, module.origin))

	# pretty print
	line = '-' * shutil.get_terminal_size().columns
	for loader, modules in loaders.items():
		print('{0}\n{1}: {2}\n{0}'.format(line, len(modules), loader))
		for module in modules:
			print('{0:30} | {1}'.format(module[0], module[1]))

	# print PYTHONPATH
	print("--------------------------- PYTHONPATH -----------------------------------------")
	try:
		user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
		print('\n'.join(user_paths))
	except:
		print("There's no PYTHONPATH")
		user_paths = []

	print("--------------------------- sys.path -------------------------------------------")
	try:
		print('\n'.join(sys.path))
	except:
		print("There's no sys.path")
		user_paths = []

	# print full path of the currently running Python
	print("--------------------------- Currently Running Python  --------------------------")
	print("Currently Running Python " , sys.version_info.major , "." , sys.version_info.minor , " : ",  sys.executable)
	print("--------------------------------------------------------------------------------")


if __name__ == '__main__':
	main()

