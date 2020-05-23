filename = 'alice.txt'

try:
	with open(filename, encoding ='utf-8') as f:
		contents = f.read()
except FileNotFoundError:
	print(f"Sorry, the file {filename} does not exist.")
else:
	#count the approx number of words in the file
	words = contents.split()
	number_of_words = len(words)
	print(f"The file {filename} has about {number_of_words} words.")