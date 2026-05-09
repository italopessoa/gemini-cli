import unittest
from src.game import SnakeGame

class TestSnakeGame(unittest.TestCase):
    def test_initialization(self):
        game = SnakeGame()
        self.assertEqual(len(game.snake), 1)
        self.assertEqual(game.snake[0], (10, 10))

    def test_move(self):
        game = SnakeGame()
        game.move()
        self.assertEqual(game.snake[0], (10, 9))

    def test_direction_change(self):
        game = SnakeGame()
        game.change_direction((1, 0))
        game.move()
        self.assertEqual(game.snake[0], (11, 10))

if __name__ == '__main__':
    unittest.main()
