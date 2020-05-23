from random import choice

lottery = [99, 51, 2, 3, 54, 17, 8, 10, 100, 69]

choice1 = choice(lottery)
choice2 = choice(lottery)
choice3 = choice(lottery)

lottery_winners = [choice1, choice2, choice3]

my_ticket = 51
count = 0
while my_ticket != lottery_winners:
	for number in lottery_winners:
		if number == my_ticket:
			break
		else:
			count += 1
			continue


print(f"And the winning ticket number is {my_ticket}! Congratulations!")
print(f"It took {count} number of iterations to get this match!")