def get_formatted_name(first_name,last_name):
	"""return a full name neatly formatted"""
	full_name = f"{first_name.title()} {last_name.title()}"
	return full_name

#this is an infinite loop
while True:
	print("\nPlease tell me your name!")
	print("Enter 'q' at any time to quit.")

	f_name = input("First name: ")
	if f_name == 'q':
		break
	l_name = input("Last name: ")
	if l_name == 'q':
		break

	formatted_name = get_formatted_name(f_name, l_name)
	print(f"Hello {formatted_name}!")