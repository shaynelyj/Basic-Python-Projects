def player_marker():
    while True:
        
        q = input("Player 1, X or O: ").upper()
    
        if q == "X":
            return ("X", "O")
        elif q == "O":
            return ("O","X")
        else:
            continue
        break
        
import random

def player_first():
    q = random.randint(0,1)
    
    if q == 0:
        return "Player1"
    else:
        return "Player2"
    
def display_board(board):
    print (f"{board[7]} | {board[8]} | {board[9]}")
    print("---------")
    print (f"{board[4]} | {board[5]} | {board[6]}")
    print("---------")
    print (f"{board[1]} | {board[2]} | {board[3]}")
    
def space_check(board,position):
    return board[position] == " "

def full_check(board):
    for a in range(1,10):
        if space_check(board,a):
            return False
    return True

def player_position(board,marker):
    while True:
        try:
            q = int(input("Position: "))
        except:
            print("Select integer 1 - 9")
        else:
            if not space_check(board,q):
                print ("Position taken up")
                continue
            else:
                board[q] = marker
                break

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

while True:
    
    playing = True
    print ("Welcome to Tic Tac Toe!")
    player1_marker,player2_marker = player_marker()
    turn = player_first()
    print (f"{turn} will go first\n")
    
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    
    while playing:
    
        if turn == "Player1":
            display_board(board)
            print ("")
            player_position(board,player1_marker)
            print ("")

            if win_check(board,player1_marker):
                display_board(board)
                print ("\nPlayer 1 wins!")
                playing = False
            elif full_check(board):
                display_board(board)
                print ("\nTie!")
                playing = False
            else:
                turn = "Player2"
                
        else:
            display_board(board)
            print ("")
            player_position(board,player2_marker)
            print ("")

            if win_check(board,player2_marker):
                display_board(board)
                print ("\nPlayer 2 wins!")
                playing = False
            elif full_check(board):
                display_board(board)
                print ("\nTie!")
                playing = False
            else:
                turn = "Player1"
                
                
    replay = input("Play again? Y or N: ").lower()
    
    if replay == "y":
        playing = True
        continue
    else:
        print ("Thanks for playing!")
        break
