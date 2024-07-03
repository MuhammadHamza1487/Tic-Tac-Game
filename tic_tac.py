def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

def check_win(board, player):
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2] == player) or (board[0][i] == board[1][i] == board[2][i] == player):
            return True
    
    if (board[0][0] == board[1][1] == board[2][2] == player) or (board[0][2] == board[1][1] == board[2][0] == player):
        return True
    
    return False


def check_draw(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def move(player):
    while True:
        try:
            row = int(input(f"Player {player}, enter the row : ")) - 1
            col = int(input(f"Player {player}, enter the column : ")) - 1
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Invalid input. Please enter numbers between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter valid integers.")

def play_game():
    board = []
    for _ in range(3):
        row = [' '] * 3
        board.append(row)

    current_player = 'X'
    
    while True:
        print_board(board)
        row, col = move(current_player)
        
        if board[row][col] != ' ':
            print("Cell already taken. Choose another one.")
            continue
        
        board[row][col] = current_player
        
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins")
            break
        
        if check_draw(board):
            print_board(board)
            print("The game is draw!")
            break
        
        if current_player == 'X':
            current_player = 'O' 
        else:
            current_player = 'X' 

play_game()
