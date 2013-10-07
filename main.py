import movement
import help
import inventory

location = [4, 4]
play = 1
items = {}
currentInventory = {}

while play == 1:

    #Defining object locations
    items.clear()
    if location == [4,4]:
        inventory.addItems(location, items, currentInventory, 'apple')
    elif location == [4,5]:
        inventory.addItems(location, items, currentInventory, 'orange')

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
        inventory.take(commands[1], items, currentInventory)

    elif commands[0] == 'inv':
        for value in currentInventory.values():
            print(value)

    elif commands[0] == 'search':
        print(items)
