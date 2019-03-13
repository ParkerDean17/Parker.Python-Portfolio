# Parker Dean
# 2-13-19

import cards


def ask_yes_no(question):
    """ Ask a yes or no question and only want yes or no."""
    response = None
    while response not in ("yes","no"):
        response = input(question).lower()
    return response


def ask_number(question,low,high):
    """Ask for a number within a range."""
    response = None
    while True:
        try:
            response = int(input(question))
            if response in range(low, high):
                return response
            else:
                print("Thats out of range.")
        except:
            print("That's not a number.")


def next_turn(turn):
    """ A change in turns."""
    if turn == X:
        return O
    else:
        return X


def switch_turn(num_players, turn):
    """ A change in turns."""
    if turn < num_players - 1:
        turn += 1
    else:
        turn = 0
    return turn


def congrat_winner(the_winner, computer, human):
    """ A winner is announced at the end of a game versus a computer."""
    if the_winner != TIE:
        print(the_winner, "won!\n")
    else:
        print("It's a tie.\n")

    if the_winner == computer:
        print("As I predicted, human, I am triumphant once more.\n" +
              "Proof that computers are superior to humans in all regards.")
    elif the_winner == human:
        print("No, no!  It cannot be!  Somehow you tricked me, human. \n" +
              "But never again!  I, the computer, so swear it!")
    elif the_winner == TIE:
        print("You were most lucky, human, and somehow managed to tie me.  \n"+
              "Celebrate today... for this is the best you will ever achieve.")


def winner_grats(winner):
    """ A winner is announced at the end of a game versus someone else."""
    print("Congradulations!!!")
    print("The winner is", winner)
    print()
    input("press enter to exit")


def roll(self):
    import random
    die1 = random.randint(1,6)
    print("You rolled a",die1)
    roll = die1
    return roll


def add_to_score(score, points):
    """ Adds points earned to a score."""
    new_score = score
    score += points
    return new_score


class Player(object):
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name
        rep = rep + " " + str(self.score)
        return rep


if __name__ == "__main__":
    print("You rand this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")