urs_food = ['ratitoulle','salmon','gummy candy','oranges','spinach','tequilla','miso','sushi','samosas']

print('the first three items in urs food are:')
for food in urs_food[:3]:
	print(food)

print('the middle three items in urs food are:')
for food in urs_food[3:6]:
	print(food)

print('the final three items in urs food are:')
for food in urs_food[6:]:
	print(food)


my_pizza = ['black olive','veggie','deepdish']
friend_pizza = my_pizza[:]
print(friend_pizza)
my_pizza.append('gluten free')
friend_pizza.append('gluten full')
print(my_pizza)
print(friend_pizza)

print('my favorite pizzas are:')
for pizza in my_pizza:
	print(pizza)

print("my friend's favorite pizzas are:")
for pizza in friend_pizza:
	print(pizza)