from random import choice

my_number = [51]
count = 0

while True:
	lottery = [99, 51, 2, 3, 54, 17, 8, 10, 100, 69]

	choice1 = choice(lottery)
	choice2 = choice(lottery)
	choice3 = choice(lottery)

	lottery_winners = [choice1, choice2, choice3]

	for number in lottery_winners:
		if number != my_number:
			count += 1
		else:
			break

print(f"{my_number} has been chosen!")
print(f"It only took {count} tries.. haha!")
