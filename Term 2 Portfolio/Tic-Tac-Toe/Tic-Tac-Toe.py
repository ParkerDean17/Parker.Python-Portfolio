#Parker Dean
#Tic Tac Toe

#Global Constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

#Display Instructions function
def display_instructions():
    """Display game instructions."""
    print(
    """

    Welcom to the greatest intellectual challenge of all time: Tic-Tac-Toe.
    This will be a showdown between your human brain and my silicon processor.

    You will make your mobe known by enter in number, 0 - 8. The number
    will correspond to the board position as illustated:

                 0 | 1 | 2
                 ----------
                 3 | 4 | 5
                 ----------
                 6 | 7 | 8

    Prepare yourself, the ultimate battle is about to begin. \m
    """)


#Yes or No question function
def ask_yes_no(question):
    response = None
    while response not in ("yes","no"):
        response = input(question).lower()
    return response


#Get number funciton for board
def ask_number(question,low,high):
    """Ask for a nubmer within a range."""
    response = "9999"
    while True:
        if response.isdigit():
            if int(response) in range(low, high):
                break
            else:
                response = input(question)
        else:
            print("You must enter a number")
            response = input(question)
    return int(response)


#Determine who goes first function
def pieces():
    go_first = ask_yes_no("Do you want to go first: ")
    if go_first.lower() == "yes":
        #Set player to X and Computer to O
        print("I see you hunger for the win. Take your move!\n")
        human = X
        com = O
    else:
        #Set player to O and Computer to X
        print("Coward! I will take the first move!")
        human = O
        com = X
    return com, human


#Create the board function
def new_board():
   board = []
   for squares in range(NUM_SQUARES):
       board.append(EMPTY)
   return board


#Display the board
def display_board(board):
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "_________")
    print("\n\t", board[3], "|", board[4], "|", board[5])
    print("\t", "_________")
    print("\n\t", board[6], "|", board[7], "|", board[8])


#determine moves for computer
def legal_moves(board):
    moves = []
    for square in range(len(board)):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


#Determine game winner
def winner(board):
    WAYS_TO_WIN = ((0,1,2),
            (3,4,5),
            (6,7,8),
            (0,3,6),
            (1,4,7),
            (2,5,8),
            (0,4,8),
            (2,4,6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE

    return None


#Human Move
def human_move(board):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nThat square is already occupied, foolish human.")
    print("Fine...")
    return move
            


#Switch Turns
def next_turn(turn):
    if turn == X:
        return O
    else:
        return X

#Congratulate the Winner
def congrat_winner(the_winner, computer, human):
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

#Make computer move
def computer_move(board, computer, human):
    # make a copy to work with since function will be changing list
    board = board[:]
    # the best positions to have, in order
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("I shall take square number", end=" ")
    # if computer can win, take that move
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # done checking this move, undo it
        board[move] = EMPTY

    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # done checking this move, undo it
        board[move] = EMPTY

    # since no one can win on next move, pick best open square
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

def main():
    display_instructions()
    com, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board)
            board[move] = human
        else:
            move = computer_move(board, com, human)
            board[move] = com
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, com, human)

main()





    



