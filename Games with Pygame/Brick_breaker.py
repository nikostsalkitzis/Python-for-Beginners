import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15
BALL_SIZE = 10
BRICK_WIDTH = 60
BRICK_HEIGHT = 20
ROWS = 5
COLS = 10
BRICK_PADDING = 10
PADDLE_SPEED = 6
BALL_SPEED = 5
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brick Breaker")

# Font setup
font = pygame.font.SysFont(None, 36)

# Paddle class
class Paddle:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2
        self.y = SCREEN_HEIGHT - PADDLE_HEIGHT - 10
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.color = BLUE
        self.speed = PADDLE_SPEED

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self, dx):
        self.x += dx
        self.x = max(0, min(SCREEN_WIDTH - self.width, self.x))

# Ball class
class Ball:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.size = BALL_SIZE
        self.color = RED
        self.dx = BALL_SPEED
        self.dy = -BALL_SPEED

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Bounce off the walls
        if self.x <= self.size or self.x >= SCREEN_WIDTH - self.size:
            self.dx *= -1
        if self.y <= self.size:
            self.dy *= -1

# Brick class
class Brick:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = BRICK_WIDTH
        self.height = BRICK_HEIGHT
        self.color = GREEN
        self.hit = False

    def draw(self):
        if not self.hit:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

def display_message(message, color):
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)

def main():
    clock = pygame.time.Clock()
    running = True
    game_over = False
    game_won = False

    paddle = Paddle()
    ball = Ball()

    # Create bricks
    bricks = []
    for row in range(ROWS):
        for col in range(COLS):
            x = col * (BRICK_WIDTH + BRICK_PADDING) + BRICK_PADDING
            y = row * (BRICK_HEIGHT + BRICK_PADDING) + BRICK_PADDING
            bricks.append(Brick(x, y))

    score = 0

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if not game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                paddle.move(-paddle.speed)
            if keys[pygame.K_RIGHT]:
                paddle.move(paddle.speed)

            ball.move()

            # Ball and paddle collision
            if (paddle.x < ball.x < paddle.x + paddle.width) and (paddle.y < ball.y + ball.size < paddle.y + paddle.height):
                ball.dy *= -1

            # Ball and brick collision
            for brick in bricks[:]:
                if (brick.x < ball.x < brick.x + brick.width) and (brick.y < ball.y < brick.y + brick.height):
                    ball.dy *= -1
                    bricks.remove(brick)
                    score += 10
                    break

            # Check if ball falls below the paddle
            if ball.y > SCREEN_HEIGHT:
                game_over = True

            # Check if all bricks are broken
            if not bricks:
                game_won = True
                game_over = True

            paddle.draw()
            ball.draw()
            for brick in bricks:
                brick.draw()

            # Display score
            score_text = font.render(f"Score: {score}", True, WHITE)
            screen.blit(score_text, (10, 10))

        if game_over:
            if game_won:
                display_message("You Win!", GREEN)
            else:
                display_message("Game Over", RED)
                
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
