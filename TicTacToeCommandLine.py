class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 3x3 TicTacToe board
        self.current_winner = None  # keep track of winner!

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check the row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([s == letter for s in row]):
            return True
        # check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([s == letter for s in column]):
            return True
        # check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # left to right diagonal
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # right to left diagonal
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def play_game(self):
        self.print_board_nums()
        letter = 'X'  # starting letter
        # iterate while the game still has empty squares
        # (we don't have to worry about winner because we'll just return that
        # which breaks the loop)
        while self.available_moves():
            square = self.choose_move(letter)
            if self.make_move(square, letter):
                print(f'{letter} makes a move to square {square}')
                self.print_board()
                if self.current_winner:
                    print(f'{letter} wins!')
                    return
                letter = 'O' if letter == 'X' else 'X'  # switches player
            else:
                print('This square is already filled. Choose another!')
        print("It's a tie!")

    def choose_move(self, letter):
        valid_square = False
        val = None
        while not valid_square:
            square = input(f'{letter}\'s turn. Input move (0-8): ')
            # check that this is a correct value by trying to cast it to an integer, and if it's not, then we say its invalid
            # if that spot is not available on the board, we also say its invalid
            try:
                val = int(square)
                if val not in self.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val

game = TicTacToe()
game.play_game()
