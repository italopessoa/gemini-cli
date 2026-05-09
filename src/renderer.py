import os

class Renderer:
    def __init__(self, game):
        self.game = game

    def render(self):
        # Clear screen
        os.system('clear')
        
        # Draw grid
        board = [[' ' for _ in range(self.game.width)] for _ in range(self.game.height)]
        
        for x, y in self.game.snake:
            if 0 <= x < self.game.width and 0 <= y < self.game.height:
                board[y][x] = '#'
        
        print('+' + '-' * self.game.width + '+')
        for row in board:
            print('|' + ''.join(row) + '|')
        print('+' + '-' * self.game.width + '+')
