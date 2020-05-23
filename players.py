players = ['chris','leo','josie','morgan','jess']
print(players)

print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[3:])
print(players[-1:])
print(players[:-2])

print("\nHere are the first three players in my team:")
for player in players[:-2]:
	print(player.title())

