sandwitch_orders = ['meatball marinara','italian','blt','bacon egg swiss','veggie','pastrami']
sandwitch_orders += ['pastrami','pastrami']
finished_sandwitches = []

print("The deli has run out of pastrami today.")

while 'pastrami' in sandwitch_orders:
	sandwitch_orders.remove('pastrami')

while sandwitch_orders:
	complete = sandwitch_orders.pop()
	print(f"I made your {complete} sandwitch!")
	finished_sandwitches.append(complete)

print("Each sandwitch has been made.")