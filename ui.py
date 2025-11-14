# ui.py

import tkinter as tk
from tkinter import messagebox
from game_logic import TicTacToe

game = TicTacToe()

root = tk.Tk()
root.title("Крестики-нолики")

buttons = [[None for _ in range(3)] for _ in range(3)]

def update_ui():
    for r in range(3):
        for c in range(3):
            buttons[r][c].config(text=game.board[r][c])

def on_click(r, c):
    if not game.make_move(r, c):
        return

    update_ui()

    if game.check_winner():
        messagebox.showinfo("Победа!", f"Игрок {game.current_player} выиграл!")
        game.reset()
        update_ui()
        return

    game.switch_player()

for r in range(3):
    for c in range(3):
        buttons[r][c] = tk.Button(
            root,
            text=" ",
            width=8, height=4,
            font=("Arial", 20, "bold"),
            command=lambda r=r, c=c: on_click(r, c)
        )
        buttons[r][c].grid(row=r, column=c, padx=5, pady=5)

root.mainloop()
