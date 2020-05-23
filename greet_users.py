def greet_users(names):
	"""function that greets users"""
	for name in names:
		msg = f"Hello, {name.title()}!"
		print(msg)

users = ['frank','ethan', 'pink guy']
greet_users(users)