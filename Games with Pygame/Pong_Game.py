import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
BALL_SIZE = 20
PADDLE_SPEED = 7
BALL_SPEED_X = 5
BALL_SPEED_Y = 5
FPS = 60
POWER_UP_SIZE = 20

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Enhanced Pong")

# Font setup
font = pygame.font.SysFont(None, 55)

# Paddle class
class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.color = WHITE
        self.speed = PADDLE_SPEED

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self, dy):
        self.y += dy
        self.y = max(0, min(SCREEN_HEIGHT - self.height, self.y))

# Ball class
class Ball:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.size = BALL_SIZE
        self.color = WHITE
        self.dx = BALL_SPEED_X * random.choice((1, -1))
        self.dy = BALL_SPEED_Y * random.choice((1, -1))

    def draw(self):
        pygame.draw.ellipse(screen, self.color, (self.x, self.y, self.size, self.size))

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Bounce off top and bottom walls
        if self.y <= 0 or self.y >= SCREEN_HEIGHT - self.size:
            self.dy *= -1

# PowerUp class
class PowerUp:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH - POWER_UP_SIZE)
        self.y = random.randint(0, SCREEN_HEIGHT - POWER_UP_SIZE)
        self.size = POWER_UP_SIZE
        self.color = GREEN

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

def display_message(message, color):
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)

def main():
    clock = pygame.time.Clock()
    running = True

    paddle_left = Paddle(10, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
    paddle_right = Paddle(SCREEN_WIDTH - 30, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
    ball = Ball()
    power_up = PowerUp()

    left_score = 0
    right_score = 0

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle_left.move(-paddle_left.speed)
        if keys[pygame.K_s]:
            paddle_left.move(paddle_left.speed)
        if keys[pygame.K_UP]:
            paddle_right.move(-paddle_right.speed)
        if keys[pygame.K_DOWN]:
            paddle_right.move(paddle_right.speed)

        ball.move()

        # Ball and paddles collision
        if (ball.x <= paddle_left.x + paddle_left.width and
            paddle_left.y < ball.y + ball.size and
            ball.y < paddle_left.y + paddle_left.height):
            ball.dx *= -1

        if (ball.x + ball.size >= paddle_right.x and
            paddle_right.y < ball.y + ball.size and
            ball.y < paddle_right.y + paddle_right.height):
            ball.dx *= -1

        # Ball out of bounds
        if ball.x < 0:
            right_score += 1
            ball = Ball()  # Reset ball
        if ball.x > SCREEN_WIDTH:
            left_score += 1
            ball = Ball()  # Reset ball

        # Power-up collision
        if (power_up.x < ball.x < power_up.x + POWER_UP_SIZE and
            power_up.y < ball.y < power_up.y + POWER_UP_SIZE):
            # Handle power-up effect here
            power_up = PowerUp()  # Reset power-up

        paddle_left.draw()
        paddle_right.draw()
        ball.draw()
        power_up.draw()

        # Draw scores
        score_text = font.render(f"{left_score}   {right_score}", True, WHITE)
        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 20))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
