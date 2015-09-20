__author__ = 'Eddie'

import deck
import itertools

class Board:
    """
    Board object to hold the cards.
    """

    def __init__(self, deck=deck.Deck()):
        """
        Initalization function for board
        :param deck: Deck object
        :return: None
        """
        self.card_list = []
        self.card_rem_list = []
        self.deck = deck

        # Initialize board state with 12 cards
        for i in range(0, 12):
            self.add_card()

    def is_set(self, card1, card2, card3):
        """
        Determines whether or not three cards are in a set

        There are three values for each property of a card which I assign 0, 1, and 2.

        If a property of three cards have the same value, it can be 0,0,0, 1,1,1, and 2,2,2, which add up to
        0, 3, and 6 respectively.

        If a feature of three cards have all different values, then it can be 0,1,2, 0,2,1, 1,2,0 1,0,2, 2,0,1, 2,1,0
        all of which sum to 3.

        As a result, we can just sum the values of each property for the three cards and mod 3 them, if there is no
        remainder, then we know that the respective property restraint is satisfied.

        :param card1: Card object
        :param card2: Card object
        :param card3: Card object
        :return: True if these cards are in a set, False otherwise.
        """
        if (
            (card1.color + card2.color + card3.color) % 3 == 0 and
            (card1.shape + card2.shape + card3.shape) % 3 == 0 and
            (card1.shading + card2.shading + card3.shading) % 3 == 0 and
            (card1.number + card2.number + card3.number) % 3 == 0):
            return True
        return False

    def get_set_on_board(self):
        """
        Determines whether or not this board contains a set

        The card's value total / 3 remainder is used to pick only groups of three cards that have the possibility
        to be sets. This is because since for three cards to be a set, each of their property values sums mod 3 must
        be equal to zero, so the sum of all property values mod 3 must also equal to zero.

        The only two possibilities of total mod 3 equaling 0, is if the remainders are 1,1,1 and 0,1,2, so we can
        reduce the number of combinations we have to check by only checking these groups.

        :return: List containing the indexes of the three cards in self.card_list if set is found. None otherwise
        """

        # Check for 1,1,1 first
        rem_1_list = []
        for i in range(0, len(self.card_rem_list)):
            if self.card_rem_list[i] == 1:
                rem_1_list.append(i)

        # Get all combinations of rem_1_list
        possible_set_list = list(itertools.combinations(rem_1_list, 3))

        for p_set in possible_set_list:
            if self.is_set(self.card_list[p_set[0]], self.card_list[p_set[1]], self.card_list[p_set[2]]):
                p_set = list(p_set)
                p_set.sort(reverse=True)
                return p_set

        # Check for 0,1,2
        idx_list = [[],[],[]]
        for i in range(0, len(self.card_rem_list)):
            idx_list[self.card_rem_list[i]].append(i)

        for i in range(0, len(idx_list[0])):
            for j in range(0, len(idx_list[1])):
                for k in range(0, len(idx_list[2])):
                    if self.is_set(self.card_list[idx_list[0][i]], self.card_list[idx_list[1][j]], self.card_list[idx_list[2][k]]):
                        set = [idx_list[0][i], idx_list[1][j], idx_list[2][k]]
                        set.sort(reverse=True)
                        return set

        # No valid set found on board
        return None

    def add_card(self):
        """
        Gets a new card from the deck and adds it to the board.
        :return: Card if available, None otherwise.
        """
        new_card = self.deck.deal_card()
        if new_card == None:        # Empty deck
            return None

        self.card_list.append(new_card)
        self.card_rem_list.append(new_card.rem)

        return new_card

    def remove_card(self, card_idx):
        """
        Removes a card from the board and returns it.
        :param card_idx: index of the card in self.card_list
        :return: Card object
        """
        self.card_rem_list.pop(card_idx)
        return self.card_list.pop(card_idx)

    def is_gameover(self):
        """
        Returns True if the game is over. False otherwise.
        :return: Boolean
        """
        if (len(self.card_list) == 0) and self.deck.is_deck_empty():
            return True
        return False

