import math


def print_board(board):
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()


def check_winner(board):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    if " " not in board:
        return "Draw"

    return None


def minimax(board, depth, is_ai_turn):
    result = check_winner(board)

    if result == "O":
        return 10 - depth

    if result == "X":
        return depth - 10

    if result == "Draw":
        return 0

    if is_ai_turn:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"

                score = minimax(board, depth + 1, False)

                board[i] = " "

                best_score = max(best_score, score)

        return best_score

    best_score = math.inf

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"

            score = minimax(board, depth + 1, True)

            board[i] = " "

            best_score = min(best_score, score)

    return best_score


def find_best_move(board):
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"

            score = minimax(board, 0, False)

            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    return best_move


def player_move(board):
    while True:
        try:
            position = int(input("Enter your position (1-9): "))

            if position < 1 or position > 9:
                print("Please enter a number from 1 to 9.")
                continue

            index = position - 1

            if board[index] != " ":
                print("That position is already taken.")
                continue

            board[index] = "X"
            break

        except ValueError:
            print("Please enter a valid number.")


def play_game():
    board = [" "] * 9

    print("\nWelcome to Tic-Tac-Toe AI!")
    print("You are X and the computer is O.")
    print("Choose a position from 1 to 9.")

    print()
    print(" 1 | 2 | 3")
    print("---+---+---")
    print(" 4 | 5 | 6")
    print("---+---+---")
    print(" 7 | 8 | 9")

    while True:

        print_board(board)

        player_move(board)

        result = check_winner(board)

        if result:
            print_board(board)

            if result == "X":
                print("You win!")

            else:
                print("It's a draw!")

            break

        print("Computer is thinking...")

        move = find_best_move(board)

        if move is not None:
            board[move] = "O"

        result = check_winner(board)

        if result:
            print_board(board)

            if result == "O":
                print("Computer wins!")

            else:
                print("It's a draw!")

            break


def main():
    while True:

        play_game()

        again = input("\nDo you want to play again? (y/n): ").lower()

        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
