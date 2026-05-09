class SnakeGame:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.snake = [(width // 2, height // 2)]
        self.direction = (0, -1)  # Up

    def move(self):
        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        self.snake.insert(0, new_head)
        self.snake.pop()

    def change_direction(self, new_direction):
        # Prevent 180 degree turns
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction
