import math

from sense_hat import SenseHat
sense = SenseHat()

# Screen width and height in pixels
WIDTH = 600
HEIGHT = 400

# Number of pixels that bullets move for each update
SPEED = 20

# Number of seconds between bullet shots
INTERVAL = 0.1

# Maximum rotation needed to reach edge of screen in degrees
DEG = 20

# Time left for game in seconds
time_left = 15

# Whether game is over
game_over = False

# Actor object that represents player1
player1 = Actor('penguin', midleft=(0, HEIGHT // 2))

# List of bullets that player1 has shot
player1_bullets = []

# player1's score
player1_score = 0

# Actor object that represents player2
player2 = Actor('penguin', midright=(WIDTH, HEIGHT // 2))

# List of bullets that player2 has shot
player2_bullets = []

# player2's score
player2_score = 0


def draw():
    screen.clear()

    # Show time left and scores no matter what
    time_msg = 'Time Left: ' + str(time_left)
    screen.draw.text(time_msg, midtop=(WIDTH // 2, 0))
    player1_msg = 'Player 1 Score: ' + str(player1_score)
    screen.draw.text(player1_msg, topleft=(0, 0))
    player2_msg = 'Player 2 Score: ' + str(player2_score)
    screen.draw.text(player2_msg, topright=(WIDTH, 0))

    # Show winner if game is over
    if game_over:
        msg = 'DRAW!'
        if player1_score > player2_score:
            msg = 'PLAYER 1 WINS!'
        elif player2_score > player1_score:
            msg = 'PLAYER 2 WINS!'
        screen.draw.text(msg, center=(WIDTH // 2, HEIGHT // 2),
                         fontsize=72)
        return

    # Draw player1
    player1.draw()

    # Draw player2
    player2.draw()

    # Draw player1_bullets
    for b in player1_bullets:
        b.draw()

    # Draw player2_bullets
    for b in player2_bullets:
        b.draw()


def on_mouse_move(pos):
    # Update position of player1
    player1.y = pos[1]


def update():
    global player1_score
    global player2_score

    if game_over:
        return

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

    # Update positions of player1_bullets
    for index in reversed(range(len(player1_bullets))):
        b = player1_bullets[index]
        b.x += SPEED
        if b.x >= WIDTH:
            player1_bullets.pop(index)
        elif b.colliderect(player2):
            player1_score += 1
            player1_bullets.pop(index)

    # Update positions of player2_bullets
    for index in reversed(range(len(player2_bullets))):
        b = player2_bullets[index]
        b.x -= SPEED
        if b.x < 0:
            player2_bullets.pop(index)
        elif b.colliderect(player1):
            player2_score += 1
            player2_bullets.pop(index)


def fire_bullets():
    player1_bullets.append(Actor('token1', player1.pos))
    player2_bullets.append(Actor('token2', player2.pos))


def countdown():
    global game_over
    global time_left

    if game_over:
        return

    time_left -= 1
    if time_left == 0:
        game_over = True
        sense.clear()


clock.schedule_interval(fire_bullets, INTERVAL)
clock.schedule_interval(countdown, 1)
