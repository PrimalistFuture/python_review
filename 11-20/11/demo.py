# Blackjack

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
# CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random

def start_game():
    """Initializes blackjack"""
    player = {"name": "player", "score": 0, "hand": [], "bust": False, "winner": False}
    dealer = {"name": "dealer", "score": 0, "hand": [], "bust": False, "winner": False}

    draw_cards_and_add_to_hand(player, 2)
    draw_cards_and_add_to_hand(dealer, 2)
    print(f"Your hand is {player['hand']}.")
    print(f"The dealer's hand is {dealer['hand']}.")

    player["score"] = handle_scoring(player["hand"])
    dealer["score"] = handle_scoring(dealer["hand"])
    print(f"Your score is {player['score']}.")
    print(f"The dealer's score is {dealer['score']}.")

    return player, dealer

def handle_scoring(hand):
    """Takes in a hand list, and returns the score, using the lower value of aces '1' if the score is over 21."""
    # TODO: handle aces better. Right now only checks to use the lower value if the total is over 21 and the current card is an ace, which isn't nearly as often as it should.
    total = 0
    for card in hand:
        if card == 11 and total > 21:
            card = 1
        total += card
    return total


def determine_bust(gamblers):
    """Accepts list of players and dealer dictionaries, and determines if a bust has occurred."""
    target_score = 21
    for gambler in gamblers:
        if gambler["name"] == "player" and gambler["score"] > target_score:
            gambler["bust"] = True
            # return f"{gambler['name']} has busted."
            return True
        elif gambler["name"] == "dealer" and gambler["score"] > target_score:
            gambler["bust"] = True
            # return f"{gambler['name']} has busted."
            return True
    return False


def draw_cards_and_add_to_hand(gambler_dict, cards_to_draw):
    """Accepts a dictionary of either a player or the dealer, and a number of cards to draw.
    Returns the dictionary with the updated hand"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    drawn_cards = random.sample(cards, cards_to_draw)
    hand = gambler_dict["hand"]
    for card in drawn_cards:
        hand.append(card) 
    return gambler_dict


def determine_winner_on_score(gamblers):
    """Accepts a list of gambler objects, and determines the winner."""
    high_score = -1
    tied = False
    for gambler in gamblers:
        if gambler["score"] > high_score:
            high_score = gambler["score"]
        elif gambler["score"] == high_score:
            tied = True
    if tied is True:
        return f"The game is tied."
    else:
        for gambler in gamblers:
            if gambler["score"] == high_score:
                gambler["winner"] = True
                return f"{gambler['name']} is the winner with a score of {gambler['score']}"
        

def direct_game():
    """Main function controlling the flow of blackjack"""
    player, dealer = start_game()

    response = input("Would you like to hit? Type 'y' for yes, or 'n' to stand.")
    if response == 'y':
        while (player["bust"] is False and dealer["bust"] is False) and response == 'y':
            # Player flow
            draw_cards_and_add_to_hand(player, 1)
            print(f"Your hand is {player['hand']}.")
            player["score"] = handle_scoring(player["hand"])
            print(f"Your score is {player['score']}.")
            # Check bust
            isBust = determine_bust([player])
            if isBust:
                print(f"{dealer['name']} busts and the player is the winner.")
                return 
            # Dealer hits if their score is less than player
            if dealer["score"] < player["score"]:
                draw_cards_and_add_to_hand(dealer, 1)
                print(f"The dealer's hand is {dealer['hand']}.")
                dealer["score"] = handle_scoring(dealer["hand"])
                print(f"The dealer's score is {dealer['score']}.")
            # Check bust on dealer
            isBust = determine_bust([dealer])
            if isBust:
                print(f"{dealer['name']} busts and the player is the winner.")
                return 
            # hit again?
            response = input("Would you like to hit? Type 'y' for yes, or 'n' to stand.")
    if response == 'n':
        while dealer["score"] < player["score"]:
            # dealer hits if score is less than player
            if dealer["score"] < player["score"]:
                draw_cards_and_add_to_hand(dealer, 1)
                print(f"The dealer's hand is {dealer['hand']}.")
                dealer["score"] = handle_scoring(dealer["hand"])
                print(f"The dealer's score is {dealer['score']}.")
            # Check bust on dealer
            isBust = determine_bust([dealer])
            if isBust:
                print(f"{dealer['name']} busts and the player is the winner.")
                return
    winner = determine_winner_on_score([player, dealer])
    print(winner) 

direct_game()