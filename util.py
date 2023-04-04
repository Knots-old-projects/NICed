import json
import pathlib
import os

def load_json(path):
	"""
	Load a json file
	"""
	
	try:
		return json.loads(pathlib.Path(path).read_text())
	except FileNotFoundError as e:
		return None

def save_json(path, data):
	"""
	Save a json file
	"""
	
	pathlib.Path(path).write_text(json.dumps(data))

def load_text(path):
	return pathlib.Path(path).read_text()

def run(cmd):
	"""
	Run a command
	"""
	
	return os.system(cmd)
