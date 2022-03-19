"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

def value_of_card(card):
    """Determine the scoring value of a card."""
    if card == 'A':
        return 1
    elif card in ['J', 'K', 'Q']:
        return 10
    return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand."""
    n_card_one = value_of_card(card_one)
    n_card_two = value_of_card(card_two)

    if n_card_one > n_card_two:
        return card_one
    elif n_card_two > n_card_one:
        return card_two
    return card_one, card_two
    

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card."""
    n_card_one = value_of_card(card_one)
    n_card_two = value_of_card(card_two)

    if card_one == 'A' or card_two == 'A':
        return 1
    elif n_card_one + n_card_two + 11 <= 21:
        return 11
    return 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'."""
    
    if card_one == 'A' and card_two == 'A':
        return False
    elif card_one == 'A' and card_two in ['10', 'J', 'K', 'Q']:
        return True
    elif card_two == 'A' and card_one in ['10', 'J', 'K', 'Q']:
        return True
    return False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands."""
    n_card_one = value_of_card(card_one)
    n_card_two = value_of_card(card_two)

    if n_card_one == n_card_two:
        return True
    return False


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet."""
    n_card_one = value_of_card(card_one)
    n_card_two = value_of_card(card_two)

    if n_card_one + n_card_two in [9, 10, 11]:
        return True
    return False
