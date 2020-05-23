def make_car(manufacturer, model, **description):
	"""building a dictionary about a car"""
	description['manufacturer'] = manufacturer
	description['car model'] = model
	return description

scion_tc = make_car('scion','tc 2006', color = 'dark gray', style = 'hatchback')

print(scion_tc)
