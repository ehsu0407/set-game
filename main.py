__author__ = 'Eddie'

import board

def main():
    """
    Main function to run a full game of Sets
    :return: None
    """

    my_board = board.Board()
    removed_sets_list = []
    game_over = False
    while not my_board.is_gameover() and not game_over:

        # First check to see if any sets are available for taking
        set_idx_list = my_board.get_set_on_board()
        if set_idx_list is not None:
            # Set found, take the set and restart
            set = (
                my_board.remove_card(set_idx_list[0]),
                my_board.remove_card(set_idx_list[1]),
                my_board.remove_card(set_idx_list[2])
            )

            print "Removed Set:"
            for i in range(0, 3):
                set[i].print_info()

            removed_sets_list.append(set)
            continue

        # No sets available to take, deal 3 new cards.
        for i in range(0, 3):
            new_card = my_board.add_card()
            if new_card is None:
                # No cards left in deck and no possible sets on board.
                game_over = True
            else:
                print "Added Card:"
                new_card.print_info()

    # Game over, print the list of cards remaining
    print "Remaining Cards"
    for card in my_board.card_list:
        card.print_info()

    return removed_sets_list

if __name__ == "__main__":
    main()