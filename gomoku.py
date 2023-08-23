import random

def game_menu():
    print("Welcome to the game of Gomoku!")
    print("Please select an option from the menu: ")
    print("1. Start a Game")
    print("2. Print the Board")
    print("3. Place a Stone")
    print("4. Reset the Game")
    print("5. Exit")

def create_board():
    board = [[" "] * size for _ in range(size)]
    return board


def print_board(board):
    size = len(board)

    # Print column indices
    print("  ", end="")
    for col in range(size):
        print(f" {chr(col + ord('A'))}  ", end="")
    print()

    # Print board rows with grid lines
    for row in range(size):
        print("   " + " -- " * (size - 1))
        for col in range(size):
            print(f" {board[row][col]} |", end="")
        print(f" {row}")
    print("   " + " -- " * (size - 1))


def is_occupied(board):
    for row in board:
        if " " in row:
            return False
    return True


def check_winner(board, player):
    for row in range(size):
        for col in range(size):
            if board[row][col] == player:
                # Check horizontally
                if col <= size - 5 and all(
                    board[row][col + i] == player for i in range(5)
                ):
                    return True

                # Check vertically
                if row <= size - 5 and all(
                    board[row + i][col] == player for i in range(5)
                ):
                    return True

                # Check diagonally (top-left to bottom-right)
                if (
                    row <= size - 5
                    and col <= size - 5
                    and all(board[row + i][col + i] == player for i in range(5))
                ):
                    return True

                # Check diagonally (bottom-left to top-right)
                if (
                    row >= 4
                    and col <= size - 5
                    and all(board[row - i][col + i] == player for i in range(5))
                ):
                    return True

    return False

def make_ai_move(board, player):
    while True:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)

        if board[row][col] == " ":
            board[row][col] = player
            break

def play_game():
    global size
    board = None
    mode = None
    player_x = "X"
    player_o = "O"

    while True:
        game_menu()

        choice = input("Enter your choice: ")
        while choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice. Please enter a number from 1 to 5.")
            choice = input("Enter your choice: ")

        if choice == "1":
            size = int(input("Enter board size (9, 13, 15): "))
            if size not in [9, 13, 15]:
                print("Invalid size. Please choose 9, 13, or 15.")
                continue
            board = create_board()
            player_mode = input("Select mode: Player vs. Player (pvp) or Player vs. Computer (pvc): ").lower()
            if player_mode == "pvp":
                players = [player_x, player_o]
            elif player_mode == "pvc":
                players = [player_x, "AI"]
            else:
                print("Invalid mode selection. Please choose 'pvp' or 'pvc'.")
                continue

            print("\n-------------Game started--------------")

        elif choice == "2":
            if board is None:
                print("Please start a game first.")
            else:
                print_board(board)

        elif choice == "3":
            if board is None or mode is None:
                print("Please start a game first.")

            current_player_idx = 0

            while True:
                print_board(board)
                player = players[current_player_idx]

                if player == "AI":
                    print(f"AI {player_o}'s turn:")
                    make_ai_move(board, player_o)
                else:
                    print(f"Player {player}'s turn:")
                    input_str = input("Enter row and column (row col): ")
                    row, col = map(int, input_str.split())  # Split input into row and col

                    if not (0 <= row < size and 0 <= col < size):
                        print("Invalid input. Row and column should be in the range 0-{}.".format(size - 1))
                        continue

                    if board[row][col] == " ":
                        board[row][col] = player
                    else:
                        print("Invalid move. That cell is already occupied.")
                        continue

                if check_winner(board, player):
                    print_board(board)
                    if player == "AI":
                        print(f"AI {player_o} wins!")
                    else:
                        print(f"Player {player} wins!")
                    break

                if is_occupied(board):
                    print_board(board)
                    print("It's a draw!")
                    break

                current_player_idx = 1 - current_player_idx  # Switch players

        elif choice == "4":
            board = None
            mode = None
            print("Game reset.")

        elif choice == "5":
            print("Exiting the program. Good Bye!!!")
            break

        else:
            print("Invalid choice. Please choose a valid option.")


# Start the game
play_game()


#===================================

empty = "-"
player_x = "X"
player_o = "O"
size = int(input("Enter Board Game Size 9, 13, 15: "))


def create_board():
    return [[empty for x in range(size)] for x in range(size)]


def print_board(board):
    # print("   A   B   C   D   E   F   G   H   I")
    for i in range(size):
        print("  " + chr(i + ord("A")), end=" ")
    print("\n +" + "---+" * size)
    for i, row in enumerate(board):
        print(" | " + " | ".join(row) + " |" + f"{i}")
        print(" +" + "---+" * size)
    for i in range(1, size + 1):
        print(" ", i, end=" ")
    print("\n")


# print("   A   B   C   D   E   F   G   H   I")


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
                if col <= size - 5 and all(
                    board[row][col + i] == player for i in range(5)
                ):
                    return True

                # Check vertically
                if row <= size - 5 and all(
                    board[row + i][col] == player for i in range(5)
                ):
                    return True

                # Check diagonally (top-left to bottom-right)
                if (
                    row <= size - 5
                    and col <= size - 5
                    and all(board[row + i][col + i] == player for i in range(5))
                ):
                    return True

                # Check diagonally (bottom-left to top-right)
                if (
                    row >= 4
                    and col <= size - 5
                    and all(board[row - i][col + i] == player for i in range(5))
                ):
                    return True

    return False


# Start the game
play_game()
