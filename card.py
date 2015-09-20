__author__ = 'Eddie'

S_COLOR = ["red", "green", "purple"]
S_SHAPE = ["diamond", "squiggle", "oval"]
S_SHADING = ["solid", "empty", "striped"]
S_NUMBER = ["one", "two", "three"]

class Card:
    """
    This class contains all the information for a card.
    """

    def __init__(self, color, shape, shading, number):
        """
        Initialization function. Takes a number from 0 to 2 for each parameter
        :param color: 0 - red, 1 - green, 2 - purple
        :param shape: 0 - diamond, 1 - squiggle, 2 - oval
        :param shading: 0 - solid, 1 - empty, 2 - striped
        :param number: 0 - one, 1 - two, 2 - three
        :return: none
        """

        self.color = color
        self.shape = shape
        self.shading = shading
        self.number = number

        # This variable is used to determine potential sets
        self.rem = (color + shape + shading + number) % 3

    def print_info(self):
        """
        Prints the card's information
        :return: None
        """
        print "Card: {0}, {1}, {2}, {3}".format(S_COLOR[self.color], S_SHAPE[self.shape], S_SHADING[self.shading], S_NUMBER[self.number])
