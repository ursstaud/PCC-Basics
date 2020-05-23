from random import choice

my_number = 51
count = 0
lottery = [99,51,2,3]

while True:
	choice1 = choice(lottery)
	choice2 = choice(lottery)
	choice3 = choice(lottery)

	lottery_winners = [choice1, choice2, choice3]

	for number in lottery_winners:
		if number != my_number:
			count += 1
			print("No match, better luck next time.")
		else:
			break

print(f"{my_number} has been chosen!")
print(f"It only took {count} tries!")