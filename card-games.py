"""Card Games"""

def get_rounds(number):
    """Tracking Poker Rounds"""
    rounds = [number, number + 1, number + 2]
    return rounds
    

def concatenate_rounds(rounds_1, rounds_2):
    """Keeping all Rounds in the Same Place"""
    new_list = rounds_1 + rounds_2
    return new_list


def list_contains_round(rounds, number):
    """Finding Prior Rounds"""
    if number in rounds:
        return True 
    return False


def card_average(hand):
    """Averaging Card Values"""
    return sum(hand)/len(hand)


def approx_average_is_average(hand):
    """Alternate Averages"""
    actual_average = card_average(hand)
    average2 = (hand[0] + hand[-1])/2
    median = hand[((len(hand) + 1) // 2) -1]
    
    if actual_average in {average2, median}:
        return True
    return False


def average_even_is_average_odd(hand):
    """More Averaging Techniques"""
    even_sum = 0
    cont_even = 0
    odd_sum = 0
    cont_odd = 0
    for index in hand:
        if index % 2 == 0:
            even_sum = even_sum + index   
            cont_even = cont_even + 1
        else:
            odd_sum = odd_sum + index
            cont_odd = cont_odd + 1
    if even_sum / cont_even == odd_sum / cont_odd:
        return True
    return False


def maybe_double_last(hand):
    """Bonus Round Rules"""
    if hand[-1] == 11:
        hand[-1] = 22
        return hand
    return hand
    
