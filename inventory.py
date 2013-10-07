def addItems(location, items, currentInventory, newItems):
    items[newItems] = newItems
    if newItems in currentInventory:
        items.pop(newItems)

def take(itemName, itemsAvailable, inventory):
    inventory[itemName] = itemsAvailable[itemName]
