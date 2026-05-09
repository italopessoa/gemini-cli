import unittest
from src.game import SnakeGame

class TestSnakeGameLogic(unittest.TestCase):
    def test_initialization(self):
        game = SnakeGame(10, 10)
        self.assertEqual(game.snake, [(5, 5)])

    def test_move(self):
        game = SnakeGame(10, 10)
        game.move()
        # Initial dir (0, -1) -> (5, 4)
        self.assertEqual(game.snake, [(5, 4)])
        game.move()
        self.assertEqual(game.snake, [(5, 3)])

    def test_direction_change_invalid(self):
        game = SnakeGame(10, 10)
        # Current (0, -1). Trying (0, 1) should be ignored
        game.change_direction((0, 1))
        game.move()
        self.assertEqual(game.snake[0], (5, 4))

    def test_direction_change_valid(self):
        game = SnakeGame(10, 10)
        game.change_direction((1, 0))
        game.move()
        self.assertEqual(game.snake[0], (6, 5))

if __name__ == '__main__':
    unittest.main()
