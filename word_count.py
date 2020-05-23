def count_words(filename):
	"""count the aprox number of words in a file"""
	try:
		with open(filename, encoding= 'utf-8') as file:
			contents = file.read()
	except FileNotFoundError:
		pass
		#print(f"Sorry, the file {filename} could not be found.")
	else:
		words = contents. split()
		num_words = len(words)
		print(f"The file {filename} has about {num_words} words.")


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for filename in filenames:
	count_words(filename)