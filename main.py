import movement
import help

location = [4, 4]
play = 1

while play == 1:
	# Select an action
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