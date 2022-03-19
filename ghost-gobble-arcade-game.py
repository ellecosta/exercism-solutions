"""Ghost Gobble Arcade Game"""

def eat_ghost(power_pellet_active, touching_ghost):
    """Define if Pac-Man eats a ghost"""
    if(power_pellet_active is True and touching_ghost is True):  
        return True
    return False

def score(touching_power_pellet, touching_dot):
    """Define if Pac-Man scores"""
    if(touching_power_pellet is True or touching_dot is True):
        return True
    return False

def lose(power_pellet_active, touching_ghost):
    """Define if Pac-Man loses """
    if(touching_ghost is True and power_pellet_active is False):
        return True
    return False

def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Define if Pac-Man wins"""
    if(has_eaten_all_dots is True and lose(power_pellet_active, touching_ghost) is False):
        return True
    return False
