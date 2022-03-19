"""Cater Waiter"""

from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    """ Clean up Dish Ingredients"""
    cleaner = set(dish_ingredients)
    return (dish_name, cleaner)
    

def check_drinks(drink_name, drink_ingredients):
    """Cocktails and Mocktails"""
    for item in drink_ingredients:
        if item in ALCOHOLS:
            return drink_name + ' Cocktail'
    return drink_name + ' Mocktail'

def categorize_dish(dish_name, dish_ingredients):
    """Categorize Dishes"""
    if dish_ingredients.issubset(VEGAN) is True:
        return dish_name + ': VEGAN'
    elif dish_ingredients.issubset(VEGETARIAN) is True:
        return dish_name + ': VEGETARIAN'
    elif dish_ingredients.issubset(PALEO) is True:
        return dish_name + ': PALEO'
    elif dish_ingredients.issubset(KETO) is True:
        return dish_name + ': KETO'
    elif dish_ingredients.issubset(OMNIVORE) is True:
        return dish_name + ': OMNIVORE'
    
def tag_special_ingredients(dish):
    """Label Allergens and Restricted Foods"""
    special_notes = []
    deduplicates = set(dish[1])
    for item in deduplicates:
        if item in SPECIAL_INGREDIENTS:
            special_notes.append(item)
    special_notes_set = set(special_notes)
    return (dish[0], special_notes_set)

def compile_ingredients(dishes):
    """Compile a "Master List" of Ingredients"""
    new_dishes = set()
    for item in dishes:
        new_dishes = new_dishes | item
    return new_dishes

def separate_appetizers(dishes, appetizers):
    """Pull out Appetizers for
    Passing on Trays"""
    dishes_deduplicates = set(dishes)
    appetizers_deduplicates = set(appetizers)
    return dishes_deduplicates.difference(appetizers_deduplicates)


def singleton_ingredients(dishes, intersection):
    """Find Ingredients Used in 
    Only One Recipe"""
    new_dishes = set()
    for item in dishes:
        new_dishes = new_dishes | item
    return new_dishes.difference(intersection)
