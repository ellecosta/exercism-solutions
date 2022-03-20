"""Chaitana's Colossal Coaster"""


def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """Add me to the queue"""
    queue = []
    if ticket_type == 1:
        queue.extend(express_queue)
        queue.append(person_name)
        return queue
    elif ticket_type == 0:
        queue.extend(normal_queue)
        queue.append(person_name)
        return queue


def find_my_friend(queue, friend_name):
    """Where are my friends?"""
    return queue.index(friend_name)


def add_me_with_my_friends(queue, index, person_name):
    """Can I please join them?"""
    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue, person_name):
    """Mean Person in the queue"""
    queue.remove(person_name)
    return queue
    

def how_many_namefellows(queue, person_name):
    """Namefellows"""
    return queue.count(person_name)


def remove_the_last_person(queue):
    """Remove the last person"""
    return queue.pop(-1)


def sorted_names(queue):
    """Sort the Queue List"""
    return sorted(queue)
