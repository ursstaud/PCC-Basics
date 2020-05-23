filename = "guest.txt"

guestlist = input("Hello, what is your name so I may add you to the guest list? ")

with open(filename, 'a') as file_object:
	file_object.write(f"{guestlist.title()}\n")