"""Inventory Management"""

def create_inventory(items):
    """Create an inventory based on a list"""
    inventory = {}
    inventory = {item: items.count(item) for item in items if item not in inventory}
    return inventory

def add_items(inventory, items):
    """Add items from a list to and existing
    dictionary"""
    for item in items:
        if item in inventory:
            inventory[item] = inventory[item] + items.count(item)
            items.remove(item)
            
    for item in items:
        if item not in inventory:
            inventory[item] = items.count(item)   
    return inventory

def decrement_items(inventory, items):
    """Decrement items from the inventory"""
    for key in inventory:
        if inventory[key] - items.count(key) < 0:
            inventory[key] = 0
        else:
            inventory[key] = inventory[key] - items.count(key)
    return inventory


def remove_item(inventory, item):
    """Remove an item entirely from the inventory"""
    if item in inventory:
        del inventory[item]
        return inventory
    return inventory

def list_inventory(inventory):
    """Return the inventory content"""
    inventory_list = []
    for key in inventory:
        if inventory[key] > 0:
            inventory_list.append((key, inventory[key]))
    return inventory_list
