def city_country(city, country):
	print(f"{city.title()} is located within {country.title()}.")
	complete_string = f"{city.title()}, {country.title()}"
	print(complete_string)

city_country('paris', 'france')
city_country('santa cruz', 'united states')
city_country('montreal','canada')