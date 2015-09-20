__author__ = 'Eddie'

import card
import random

class Deck:
    """
    Object to keep track of what cards have been dealt so that unique cards are always dealt
    """
    def __init__(self):
        """
        Initialization function for Deck. Populates and shuffles the deck of cards.
        :return: None
        """
        self.card_pile = []
        for color in range(0, 3):
            for shape in range(0, 3):
                for shading in range(0, 3):
                    for number in range(0, 3):
                        self.card_pile.append(card.Card(color, shape, shading, number))

        random.shuffle(self.card_pile)

    def deal_card(self):
        """
        Deals the top card from the deck. Returns None if no cards are available to be dealt.
        :return: Card object
        """
        if self.is_deck_empty():
            return None
        return self.card_pile.pop()

    def is_deck_empty(self):
        """
        Returns True if the deck is empty, False otherwise.
        :return: Boolean
        """
        if len(self.card_pile) == 0:
            return True
        return False