favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"{language.title()}")

#taking it a step further by checking for the number of favorite languages
for name, languages in favorite_languages.items():
	if len(languages) == 1:
		print(f"\n{name.title()}'s favorite language is:")
		for language in languages:
			print(f"{language.title()}")
	else:
		print(f"\n{name.title()}'s favorite languages are:")
		for language in languages:
			print(f"{language.title()}")