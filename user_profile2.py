def build_profile(first, last, **user_info): #builds dictionary first and adds the other two values in and 
#then adds the user info first and last names in
	"""build a dictionary containing everything we know about a user"""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('albert','einstein', location='princeton', field='physics')

print(user_profile)

ursula_profile = build_profile('ursula', 'stauder', city = 'santa cruz', aspiring = 'data scientist')
print(ursula_profile)