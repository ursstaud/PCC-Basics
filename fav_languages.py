favorite_languages = {
					'jen': 'python', 
					'sarah': 'c', 
					'edward': 'ruby', 
					'phil': 'python',
					}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite langeuage is {language}.\n")

for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite programming language is {language.title()}!")
print("That is everyone's favorite languages!\n")

for name in favorite_languages.keys():
	print(name.title())

friends = ['phil','sarah']

for name in favorite_languages.keys():
	print(f"Hi {name.title()}!")
	if name in friends:
		language = favorite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
	print("Erin, please take my poll.\n\n")

for name in sorted(favorite_languages.keys()):
	print(f"{name.title()},thank you for taking my poll!\n\n")

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())

names = ['jen','sarah','edward','phil','ursula','prabhjot']

for name in names:
	if name in favorite_languages.keys():
		print("You have already taken the poll.")
	else:
		print("Please take the poll.")