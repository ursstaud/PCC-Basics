filename = "pi_million_digits.txt"

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip()

birthday = input("Please enter your birthday in the form of mmddyy: ")
if birthday in pi_string:
	print("Your birthday appears in the first million digits of pi, congratulations!")
else:
	print("Unfortunately, your birthday does not appear within the first million digits of pi. Darn!")