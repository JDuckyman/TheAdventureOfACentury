import movement
import help
import inventory

location = [4, 4]
play = 1
available = 0
apple = False
haveApple = False
orange = False
haveOrange = False

while play == 1:

	#Defining object locations
	if location == [4,4] and haveApple == False:
		apple = True
	else:
		apple = False
	if location == [4,5] and haveOrange == False:
		orange = True
	else:
		orange = False


	print(' ')
	action = input('Type what you would like to do: ')
	print(' ')
	commands = action.split()

	# Movement
	if commands[0] == 'move':
		location = movement.move(commands[1], location[0], location[1])

	# Help
	elif commands[0] == 'help':
		help.listCommands()

	#Inventory
	elif commands[0] == 'take':
		if commands[1] == 'apple' and apple == True:
			haveApple = True
		if commands[1] == 'orange' and orange == True:
			haveOrange = True


	elif commands[0] == 'inv':
			if haveApple == True:
				print('Apple')
			if haveOrange == True:
				print('Orange')