import os

class fileReader:
	path = " "
	os.chdir(path)

	def readFile(file_path):
		with open(file_path, 'r') as f:
			print (f.read())

	for file in os.listdir():
		if file.endswith(".IND" or ".ID" or ".MAP" or ".DAT"):
			file_path = f"{path}\{file}"

			readFile(file_path)