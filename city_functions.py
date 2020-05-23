def city_country(city, country, population = ''):
	if population:
		full_location = f"{city}, {country}; population: {population}"
	else:
		full_location = f"{city}, {country}"
	return full_location.title()