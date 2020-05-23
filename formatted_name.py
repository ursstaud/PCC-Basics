#when middle name is needed
def get_formatted_name(first, middle, last):
	"""return a full name, neatly formatted"""
	full_name = f"{first.title()} {middle.title()} {last.title()}"
	return full_name

ursula = get_formatted_name('ursula', 'helene','stauder')
print(ursula)


#when middle name isn't really needed
def get_formatted_name(first, last, middle = ''):
	if middle:
		full_name = f"{first.title()} {middle.title()} {last.title()}"
	else:
		full_name = f"{first.title()} {last.title()}"
	return full_name

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)