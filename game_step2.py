import math

from sense_hat import SenseHat
sense = SenseHat()

# Screen width and height in pixels
WIDTH = 600
HEIGHT = 400

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


def update():
    # Update position of player2
    orientation = sense.get_orientation()
    player2.y = (orientation['roll'] + 180) % 360
