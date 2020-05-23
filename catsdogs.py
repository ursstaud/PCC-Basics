def display_values(filename):
	try:
		with open(filename) as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		pass
		#print(f"The file {filename} cannot be found.")
	else:
		print(contents)

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
	display_values(filename)