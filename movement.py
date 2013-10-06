# Contains all functions for movement.

def move(direction, xLocation, yLocation):
	if direction == '?':
		print(str(xLocation) + ',' + str(yLocation))
	elif direction == 'north':
		yLocation = moveNorth(yLocation)
	elif direction == 'east':
		xLocation = moveEast(xLocation)
	elif direction == 'south':
		yLocation = moveSouth(yLocation)
	elif direction == 'west':
		xLocation = moveWest(xLocation)

	location = [xLocation, yLocation]
	return location


def moveNorth(yLocation):
	if yLocation < 7:
		yLocation += 1
	return yLocation

def moveEast(xLocation):
	if xLocation < 7:
		xLocation += 1
	return xLocation

def moveSouth(yLocation):
	if yLocation > 1:
		yLocation -= 1
	return yLocation

def moveWest(xLocation):
	if xLocation > 1:
		xLocation -= 1
	return xLocation
