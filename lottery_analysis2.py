from random import choice

def get_winning_ticket(possibilities):
	"""return a winning ticket from a set of possibilities"""
	winning_ticket = [] #empty list

	#we don't want to repeat winning values
	while len(winning_ticket) < 4:
		pulled_item = choice(possibilities)
		#only add the pulled item if it has not already been added
		if pulled_item not in winning_ticket:
			winning_ticket.append(pulled_item)

	return winning_ticket #repeat this 4 times then return the winning ticket

def check_ticket(played_ticket, winning_ticket):
	"""check all eleents in the played ticket, if any are 
	not in the winning ticket, return false"""
	for element in played_ticket:
		if element not in winning_ticket:
			return False

	return True #if not, return true

def make_random_ticket(possibilities):
	"""Return a random ticket from a set of possibilities"""
	ticket = []
	#we don't want to repeat letters or numbers
	while len(ticket) < 4:
		pulled_item = choice(possibilities)
		#only add to the list if it hasn't been pulled
		if pulled_item not in ticket:
			ticket.append(pulled_item)
	return ticket


possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = get_winning_ticket(possibilities)

plays = 0
won = False
max_tries = 1_000_000

while not won:
	new_ticket = make_random_ticket(possibilities)
	won = check_ticket(new_ticket, winning_ticket)
	#at the above step, if it evaluates to true, it will
	#break the loop because the while not won will
	#evaluate to false--so sneaky :P
	plays += 1 #if doesn't evaluate to true, add plays
	if plays >= max_tries:
		break #if the looped number of plays is 
		#greater than or equal to a million, stop

#if true
if won:
	print("We have a winning ticket!")
	print(f"Your ticket: {new_ticket}")
	print(f"Winning ticket: {winning_ticket}")
	print(f"It only took {plays} tries to win!")
else:
	print(f"Tried {plays} times, without pulling a winner. :(")
	print(f"Your ticket: {new_ticket}")
	print(f"Winning ticket: {winning_ticket}")