#Parker Dean
#Game List

def favorite_game_list():
    print("Here you will make a list of your favorite games of all time: ")
    game_list = []
    while True:
        option = int(input("""
        1 - Add a Game,
        2 - Remove a Game
        3 - Insert a Game,
        4 - Exit Program

        make your choice 1,2, 3, or 4
        """))
        if option == 1:
            print("this option allows you to add a game to your list. ")
            print(game_list)
            game = input("what game would you like to add to your list: ")
            game_list.append(game)
            print(game_list)
        elif option == 2:
            print("This option will allow you to remove a game from your list. ")
            print(game_list)
            while True:
                game = input("What game would you like to remove from your list")
                if game in game_list:
                    game_list.remover(game)
                    print(game_list)
                    break
                else:
                    print("That game is not on your list. ")

        elif option == 3:
            print("This option allows you to insert a game at a given position")
            game = input("What game would you like to insert in your list")
            while True:
                pos = int(input("At what position would you like to insert this game: "))
                pos -= 1
                if pos < len(game_list):
                    game_list.insert(pos,game)
                    print(game_list)
                else:
                    print("Invalid position")

        elif option == 4:
            input("Press enter to exit ")
            break
        
favorite_game_list()
