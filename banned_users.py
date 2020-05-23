banned_users = ['andrew','carolina','david','marie']
user = 'marie'

if user not in banned_users:
	print(f"{user.title()}, you can post a response if you wish.")
else:
	print("You are a banned user, therefore you may not respond. Thank you for understanding.")

	