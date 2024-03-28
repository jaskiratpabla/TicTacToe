import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.player = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.root = root
        self.initialize_ui()

    def initialize_ui(self):
        self.root.title("TicTacToe")
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text='', font=('normal', 40), height=1, width=3,
                                               command=lambda i=i, j=j: self.on_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def on_click(self, i, j):
        if self.board[i][j] == '' and self.check_winner() is None:
            self.board[i][j] = self.player
            self.buttons[i][j].config(text=self.player)
            winner = self.check_winner()
            if winner:
                messagebox.showinfo("Game Over", f"{winner} wins!")
                self.reset_game()
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            self.player = 'O' if self.player == 'X' else 'X'

    def check_winner(self):
        for row in self.board:
            if len(set(row)) == 1 and row[0] != '':
                return row[0]
        for col in zip(*self.board):
            if len(set(col)) == 1 and col[0] != '':
                return col[0]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return self.board[0][2]
        return None

    def is_draw(self):
        return all(self.board[i][j] != '' for i in range(3) for j in range(3))

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ''
                self.buttons[i][j].config(text='')

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
