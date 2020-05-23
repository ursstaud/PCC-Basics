#start witha list of users that need to be verified
#and an empty list to hold a list of users who need to be verified
unconfirmed_users = ['brian','jen','candace']
confirmed_users = []

#verify each user until there are no more unconfirmed users
#move each user to the list of confirmed users
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print(f"Verifying user: {current_user.title()}")
	confirmed_users.append(current_user)

#display all confirmed users
print("\nThe following users have been confirmed:")
for user in confirmed_users:
	print(user.title())