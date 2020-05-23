#start with some designs that need to be printed
unprinted_designs = ['robot', 'phone case', 'dodecahedron']
completed_models = []

#creating function 1
def print_models(unprinted_designs, completed_models):
	"""simulate printing each design until none are left, pop values to completed models list"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print(f"Printing model: {current_design}")
		completed_models.append(current_design)

def show_completed_models(completed_models):
	"""show all models that were completed"""
	print("\nThe following models have been completed: ")
	for complete in completed_models:
		print(complete)

unprinted_designs = ['robot', 'phone case', 'dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)