# Blackjack

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Takes a list of cards and returns the total value of the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if sum (cards) > 21 and 11 in cards:
        cards.remove(11).append(1)

    return sum(cards)

def compare(user_score, computer_score):
    """"""
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lost, opponent has blackjack."
    elif user_score == 0:
        return "Win with a blackjack."
    elif user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Opponent went over. You win."
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose."

def play_game(): 
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else: 
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else: 
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"You final hand is {user_score}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play_game()