import curses
import random

def main(stdscr):
    # Setup
    curses.curs_set(0)
    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)
    w.timeout(100)

    # State
    snk_x, snk_y = sw // 4, sh // 2
    snake = [[snk_y, snk_x], [snk_y, snk_x-1], [snk_y, snk_x-2]]
    food = [sh // 2, sw // 2]
    score = 0
    key = curses.KEY_RIGHT

    while True:
        # Render
        w.addstr(0, 2, f'Score: {score}')
        w.addch(food[0], food[1], curses.ACS_PI)

        # Input
        next_key = w.getch()
        key = key if next_key == -1 else next_key

        # Update
        new_head = [snake[0][0] + (1 if key == curses.KEY_DOWN else -1 if key == curses.KEY_UP else 0),
                    snake[0][1] + (-1 if key == curses.KEY_LEFT else 1 if key == curses.KEY_RIGHT else 0)]

        # Collision
        if (new_head[0] in [0, sh-1] or new_head[1] in [0, sw-1] or new_head in snake):
            break

        snake.insert(0, new_head)
        if snake[0] == food:
            score += 1
            food = [random.randint(1, sh-2), random.randint(1, sw-2)]
        else:
            tail = snake.pop()
            w.addch(tail[0], tail[1], ' ')

        w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD | curses.A_BOLD)

if __name__ == "__main__":
    curses.wrapper(main)
