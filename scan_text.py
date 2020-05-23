filename = 'moby_dick.txt'

with open(filename, encoding = 'utf-8') as file_object:
	content = file_object.read()

print(content.count('the '))
print(content.count('the'))


print(content.lower().count('the '))
print(content.lower().count('the'))