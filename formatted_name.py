def get_formatted_name(first, last):
	"""return a full name using return command"""
	full_name = f"{first} {last}"
	return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)