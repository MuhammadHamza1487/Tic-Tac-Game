class tic_tac:
    def __init__(self, board):
        self.board = board

    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("----------")

    def check_win(self, player):
        for i in range(3):
            if (self.board[i][0] == self.board[i][1] == self.board[i][2] == player) or (self.board[0][i] == self.board[1][i] == self.board[2][i] == player):
                return True
        
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] == player) or (self.board[0][2] == self.board[1][1] == self.board[2][0] == player):
            return True
        
        return False


    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def move(self, player):
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

    def play_game(self):
        current_player = 'X'
        
        while True:
            self.print_board()
            row, col = self.move(current_player)
            
            if self.board[row][col] != ' ':
                print("Cell already taken. Choose another one.")
                continue
            
            self.board[row][col] = current_player
            
            if self.check_win(current_player):
                self.print_board()
                print(f"Player {current_player} wins")
                break
            
            if self.check_draw():
                self.print_board()
                print("The game is draw!")
                break
            
            if current_player == 'X':
                current_player = 'O' 
            else:
                current_player = 'X'




board = []
for _ in range(3):
    row = [' '] * 3
    board.append(row)

game = tic_tac(board)
game.play_game()
