import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
PIPE_WIDTH = 50
PIPE_GAP = 150
GRAVITY = 0.25
FLAP_HEIGHT = -5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load images
bird_img = pygame.image.load("bird.png").convert_alpha()
pipe_img = pygame.image.load("pipe.png").convert_alpha()

# Scale images
bird_img = pygame.transform.scale(bird_img, (50, 50))
pipe_img = pygame.transform.scale(pipe_img, (PIPE_WIDTH, HEIGHT))

# Game variables
bird_x = 50
bird_y = HEIGHT // 2
bird_velocity = 0
pipes = []
score = 0
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

def draw():
    screen.fill(BLACK)
    screen.blit(bird_img, (bird_x, bird_y))
    for pipe in pipes:
        screen.blit(pipe_img, (pipe[0], pipe[1]))
        screen.blit(pygame.transform.flip(pipe_img, False, True), (pipe[0], pipe[2]))
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    pygame.display.update()

def generate_pipe():
    random_y = random.randint(50, HEIGHT - PIPE_GAP - 50)
    pipes.append([WIDTH, random_y, random_y + PIPE_GAP])

def game_over():
    font_large = pygame.font.Font(None, 72)
    game_over_text = font_large.render("Game Over", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 50))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    quit()

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = FLAP_HEIGHT

    bird_y += bird_velocity
    bird_velocity += GRAVITY

    if bird_y > HEIGHT - 50:
        game_over()

    if pipes:
        if pipes[0][0] < -PIPE_WIDTH:
            pipes.pop(0)

    if pipes:
        pipes[0][0] -= 3
        if pipes[0][0] == bird_x:
            score += 1

    if pipes and ((bird_x + 50 > pipes[0][0]) and (bird_x < pipes[0][0] + PIPE_WIDTH)):
        if bird_y < pipes[0][1] or bird_y + 50 > pipes[0][2]:
            game_over()

    if not pipes or pipes[-1][0] < WIDTH - 150:
        generate_pipe()

    draw()

pygame.quit()
