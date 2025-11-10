import tkinter as tk
from tkinter import messagebox

# Инициализация окна
root = tk.Tk()
root.title("Крестики-нолики")

# Игровое поле (массив)
board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"

# Функция проверки победителя
def check_winner(player):
    # Проверка строк
    for row in range(3):
        if all(board[row][col] == player for col in range(3)):
            return True
    # Проверка столбцов
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Проверка диагоналей
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Проверка, заполнено ли поле
def is_full():
    return all(board[row][col] != " " for row in range(3) for col in range(3))

# Обработка нажатия кнопки
def on_click(row, col):
    global current_player

    if board[row][col] == " ":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, state="disabled")

        if check_winner(current_player):
            messagebox.showinfo("Победа!", f"Игрок {current_player} выиграл!")
            reset_game()
        elif is_full():
            messagebox.showinfo("Ничья!", "Поле заполнено. Ничья!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"
    else:
        messagebox.showwarning("Ошибка", "Эта клетка уже занята!")

# Сброс игры
def reset_game():
    global board, current_player
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=" ", state="normal")

# Создаем кнопки для игрового поля
buttons = [[None for _ in range(3)] for _ in range(3)]
for r in range(3):
    for c in range(3):
        buttons[r][c] = tk.Button(
            root, text=" ", width=8, height=4, font=("Arial", 20, "bold"),
            command=lambda r=r, c=c: on_click(r, c)
        )
        buttons[r][c].grid(row=r, column=c, padx=5, pady=5)

# Запуск окна
root.mainloop()
