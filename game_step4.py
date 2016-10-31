import math

from sense_hat import SenseHat
sense = SenseHat()

# Screen width and height in pixels
WIDTH = 600
HEIGHT = 400

# Maximum rotation needed to reach edge of screen in degrees
DEG = 20

# Actor object that represents player1
player1 = Actor('penguin', midleft=(0, HEIGHT // 2))

# Actor object that represents player2
player2 = Actor('penguin', midright=(WIDTH, HEIGHT // 2))


def draw():
    screen.clear()

    # Draw player1
    player1.draw()

    # Draw player2
    player2.draw()


def on_mouse_move(pos):
    # Update position of player1
    player1.y = pos[1]


def update():
    # Update position of player2
    orientation = sense.get_orientation()
    # Adjust range of roll from [0, 360) to [-180, 180)
    roll = (orientation['roll'] + 180) % 360 - 180
    # Convert from degrees to pixels based on DEG
    player2.y = round((roll + DEG) / (DEG * 2) * HEIGHT)
    # Check and correct if row index is out of bounds
    if player2.y < 0:
        player2.y = 0
    elif player2.y >= HEIGHT:
        player2.y = HEIGHT - 1
