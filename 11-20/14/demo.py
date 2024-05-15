# Higher or Lower Requirements
# Comparing who has more followers on Instagram
# Keep track on the streak of correct answers
# have the user select either a or b
# Give a little bit of information on each instagramer
# if they get it right, select a new instagramer and compare them
# be functiony and run the code often

import random
import game_data
import art


def get_instagrammer():
    """Returns a random instagrammer from game_data.py"""
    return random.choice(game_data.data)


def determine_winner(insta1, insta2, as_string):
    """Takes in two game_data.data dicts, and a T / F.
    Returns the dict with the larger follower_count,
    or if T, a string of 'a' or 'b', depending on the follower count."""
    if insta1["follower_count"] > insta2["follower_count"]:
        if as_string is True:
            return 'a'
        return insta1
    else:
        if as_string is True:
            return 'b'
        return insta2


def game():
    """Conducts the game"""
    print(art.logo)
    print("Welcome to Higher Lower!")
    print("You will see two instragram accounts. Select the account that has more followers.")
    # Initializing variables
    score = 0
    game_over = False
    a = ""
    b = ""
    while game_over is False:
        # Only gets new instragrammer if one is doesn't already exist
        if a == "":
            a = get_instagrammer()
        if b == "":
            b = get_instagrammer()
        # checks for duplicates
        while a == b:
            b = get_instagrammer()

        # Will evaluate to 'a' or 'b'
        more_followers = determine_winner(a, b, True)

        print(f"""Choice a : {a['name']}, a {
              a['description']} from {a['country']}.""")
        print(art.vs)
        print(f"""Choice b: {b['name']}, a
              {b['description']} from {b['country']}.""")

        user_choice = input(
            "Who has more instragram followers? Type 'a' or 'b'. ")
        # Ends the game on wrong choice
        if user_choice is not more_followers:
            print(f"""Thats incorrect!
                  {a['name']} has {a['follower_count']} followers, and
                  {b['name']} has {b['follower_count']} followers.""")
            game_over = True
            print(f"You have lost with a score of {score}.")
        else:
            print(f"""Thats correct!
                  {a['name']} has {a['follower_count']} followers, and
                  {b['name']} has {b['follower_count']} followers.""")
            score += 1
            print(f"You have a score of {score}.")
            # Keeps the winning dict and reset loser variable
            # to fetch a new dict back at the top
            # While we already know who the winner is,
            # they are currently just a string. Probably a sharper way...
            keep_winner = determine_winner(a, b, False)
            if keep_winner == a:
                b = ""
            else:
                a = ""


game()
