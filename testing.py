import unittest

# Импортируем функции и глобальную переменную из твоего файла
from tictactoe import check_winner, is_full, board


class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        # Каждый тест начинается с чистого поля
        for r in range(3):
            for c in range(3):
                board[r][c] = " "

    def test_row_win(self):
        board[0] = ["X", "X", "X"]
        self.assertTrue(check_winner("X"))

    def test_column_win(self):
        board[0][0] = "O"
        board[1][0] = "O"
        board[2][0] = "O"
        self.assertTrue(check_winner("O"))

    def test_diagonal_win_main(self):
        board[0][0] = "X"
        board[1][1] = "X"
        board[2][2] = "X"
        self.assertTrue(check_winner("X"))

    def test_diagonal_win_reverse(self):
        board[0][2] = "O"
        board[1][1] = "O"
        board[2][0] = "O"
        self.assertTrue(check_winner("O"))

    def test_no_win(self):
        board[0] = ["X", "O", "X"]
        board[1] = ["O", "X", "O"]
        board[2] = ["O", "X", "O"]
        self.assertFalse(check_winner("O"))
        self.assertFalse(check_winner("X"))

    def test_full_board(self):
        board[0] = ["X", "O", "X"]
        board[1] = ["O", "X", "O"]
        board[2] = ["O", "X", "O"]
        self.assertTrue(is_full())

    def test_not_full_board(self):
        board[0] = ["X", " ", "O"]
        board[1] = ["O", "X", "O"]
        board[2] = ["O", "X", "O"]
        self.assertFalse(is_full())


if __name__ == "__main__":
    unittest.main()