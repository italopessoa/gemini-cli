import unittest
from src.game import SnakeGame
from src.renderer import Renderer

class TestRenderer(unittest.TestCase):
    def test_renderer_initialization(self):
        game = SnakeGame()
        renderer = Renderer(game)
        self.assertEqual(renderer.game, game)

if __name__ == '__main__':
    unittest.main()
