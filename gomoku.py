empty = "-"
player_x = "X"
player_o = "O"
size = 9

def create_board():
    return [[empty for x in range(size)] for x in range(size)]

def print_board(board):
    print("   A   B   C   D   E   F   G   H")
    print(" +" + "---+" * size)
    for i, row in enumerate(board):
        print(f"{i}| " + " | ".join(row) + " |")
        print(" +" + "---+" * size)
    print("   0   1   2   3   4   5   6   7   8")

def is_full(board):
    for row in board:
        if empty in row:
            return False
    return True

def play_game():
    while True:
        board = create_board()
        player = player_x
        
        while True:
            print_board(board)
            print(f"Player {player}'s turn:")
            
            row = int(input("Enter row (0-8): "))
            col = int(input("Enter column (0-7): "))
            
            if board[row][col] == empty:
                board[row][col] = player
            else:
                print("Invalid move. That cell is already occupied.")
                continue
            
            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break
            
            if is_full(board):
                print_board(board)
                print("It's a draw!")
                break
            
            player = player_o if player == player_x else player_x
        
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thanks for playing!")
            break

def check_winner(board, player):
    for row in range(size):
        for col in range(size):
            if board[row][col] == player:
                # Check horizontally
                if col <= size - 5 and all(board[row][col + i] == player for i in range(5)):
                    return True
                
                # Check vertically
                if row <= size - 5 and all(board[row + i][col] == player for i in range(5)):
                    return True
                
                # Check diagonally (top-left to bottom-right)
                if row <= size - 5 and col <= size - 5 and all(board[row + i][col + i] == player for i in range(5)):
                    return True
                
                # Check diagonally (bottom-left to top-right)
                if row >= 4 and col <= size - 5 and all(board[row - i][col + i] == player for i in range(5)):
                    return True
    
    return False


# Start the game
play_game()
