from random import choice

lottery = [99, 51, 2, 3, 54, 17, 8, 10, 100, 69]

choice1 = choice(lottery)
choice2 = choice(lottery)
choice3 = choice(lottery)

lottery_winners = [choice1, choice2, choice3]

print(f"Attention, these are the winning lottery numbers:")
for number in lottery_winners:
	print(number)