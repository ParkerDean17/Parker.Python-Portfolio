# Parker Dean
# 2-13-19
# High Card

import random, Cards, Games

deck = Cards.Deck()
deck.populate()
deck.shuffle()

print("Welcome to High Card.")

again = None
while again != "n":
    players = []
    num = Games.ask_number(question = "How many players? (2-10): ", low = 2, high = 11)
    for i in range(num):
        name = input("Player name: ")
        player = Games.Player(name)
        players.append(player)
    hands = []
    for player in players:
        hand = player.hand
        hands.append(hand)
    deck.deal(hands, 1)
    print("\nHere are the game results: ")
    for player in players:
        print(player)
    again = Games.ask_yes_no("\nDo you want to play again? (yes/no): ")
input("\n\nPress the enter key to exit.")