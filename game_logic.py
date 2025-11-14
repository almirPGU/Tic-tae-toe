# game_logic.py

class TicTacToe:
    def __init__(self):
        self.reset()

    def reset(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def make_move(self, r, c):
        if self.board[r][c] != " ":
            return False  # клетка занята

        self.board[r][c] = self.current_player
        return True

    def check_winner(self):
        b = self.board
        p = self.current_player

        # строки
        for row in b:
            if row.count(p) == 3:
                return True
        
        # столбцы
        for col in range(3):
            if b[0][col] == b[1][col] == b[2][col] == p:
                return True

        # диагонали
        if b[0][0] == b[1][1] == b[2][2] == p:
            return True
        if b[0][2] == b[1][1] == b[2][0] == p:
            return True

        return False

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
