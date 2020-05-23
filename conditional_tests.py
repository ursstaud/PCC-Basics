var1 = "Ursula"
var2 = "helene"
print(var1 == var2)
print(var2.upper() == 'HELENE')
print(var1.lower() == 'ursula')
print(var2.lower() == 'Helene')
print(3<1)
print(3<=3)
print(10==11)
print(4>1)
print(4>=3)
print(4>10)
print((3==3) and (4<5))
print(2<1 and 10==10)
print(2<1 or 10==10)
print(100==1 or 10==1)
print('this is a break from the booleans')
check_var = 'frank'
list_var = ['ursula','helene','kucia','stauder']
if check_var not in list_var:
	print("the full name is ursula helene kucia stauder--unhypenated!")
else: 
	print("lol who dis?")