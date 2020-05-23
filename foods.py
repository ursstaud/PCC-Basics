urs_foods =['burrito','pasta','chips']
prab_foods = urs_foods[:]
urs_foods.append('gummy candy')
prab_foods.append('cheese')
print(urs_foods)
print(prab_foods)
jess_foods = urs_foods[:2]
print(jess_foods)

for food in urs_foods:
	print(f'\n Ursula likes {food.title()}.\n')

for food in prab_foods:
	print(f'\nPrab likes {food.upper()}\n')

leo_food = ['pie','spam']
chris_food = leo_food

leo_food.append('candy')
print(chris_food)

for leo in leo_food:
	print(leo)

for chris in chris_food:
	print(chris)