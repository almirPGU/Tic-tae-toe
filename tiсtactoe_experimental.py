import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Крестики-нолики — Experimental")

board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"
vs_bot = False

def check_winner(player):
    for row in range(3):
        if all(board[row][col] == player for col in range(3)):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full():
    return all(board[row][col] != " " for row in range(3) for col in range(3))

def bot_move():
    free_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    if free_cells:
        r, c = random.choice(free_cells)
        on_click(r, c, bot=True)

def on_click(row, col, bot=False):
    global current_player

    if board[row][col] != " ":
        if not bot:
            messagebox.showwarning("Ошибка", "Клетка занята")
        return

    board[row][col] = current_player
    buttons[row][col].config(text=current_player, state="disabled")

    if check_winner(current_player):
        messagebox.showinfo("Победа!", f"Игрок {current_player} выиграл!")
        reset_game()
        return

    if is_full():
        messagebox.showinfo("Ничья!", "Поле заполнено.")
        reset_game()
        return

    current_player = "O" if current_player == "X" else "X"

    if vs_bot and current_player == "O":
        bot_move()

def reset_game():
    global board, current_player
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=" ", state="normal")

def enable_bot():
    global vs_bot
    vs_bot = True
    reset_game()

buttons = [[None for _ in range(3)] for _ in range(3)]
for r in range(3):
    for c in range(3):
        buttons[r][c] = tk.Button(
            root, text=" ", width=8, height=4, font=("Arial", 20, "bold"),
            command=lambda r=r, c=c: on_click(r, c)
        )
        buttons[r][c].grid(row=r, column=c, padx=5, pady=5)

tk.Button(root, text="Играть против бота", command=enable_bot).grid(row=3, column=0, columnspan=3)

root.mainloop()