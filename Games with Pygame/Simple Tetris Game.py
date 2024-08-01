import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)

# Tetris shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I-shape
    [[1, 1], [1, 1]],  # O-shape
    [[1, 1, 1], [0, 1, 0]],  # T-shape
    [[1, 1, 1], [1, 0, 0]],  # L-shape
    [[1, 1, 1], [0, 0, 1]],  # J-shape
    [[1, 1, 0], [0, 1, 1]],  # S-shape
    [[0, 1, 1], [1, 1, 0]]  # Z-shape
]

SHAPES_COLORS = [CYAN, YELLOW, MAGENTA, ORANGE, BLUE, GREEN, RED]

# Initialize variables
board = [[0] * 10 for _ in range(20)]
current_piece = None
current_piece_color = None
piece_x = 0
piece_y = 0
game_over = False

# Helper functions
def draw_board():
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(SCREEN, cell, pygame.Rect(x * 25, y * 25, 25, 25))

def new_piece():
    global current_piece, current_piece_color, piece_x, piece_y, game_over
    current_piece = random.choice(SHAPES)
    current_piece_color = random.choice(SHAPES_COLORS)
    piece_x = 3
    piece_y = 0
    if not is_valid_move():
        game_over = True

def draw_piece():
    for y, row in enumerate(current_piece):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(SCREEN, current_piece_color,
                                 pygame.Rect((piece_x + x) * 25, (piece_y + y) * 25, 25, 25))

def move_down():
    global piece_y, game_over
    piece_y += 1
    if not is_valid_move():
        piece_y -= 1
        place_piece()
        new_piece()

def move_left():
    global piece_x
    piece_x -= 1
    if not is_valid_move():
        piece_x += 1

def move_right():
    global piece_x
    piece_x += 1
    if not is_valid_move():
        piece_x -= 1

def rotate_piece():
    global current_piece
    current_piece = list(map(list, zip(*reversed(current_piece))))
    if not is_valid_move():
        current_piece = list(map(list, zip(*reversed(current_piece))))

def is_valid_move():
    for y, row in enumerate(current_piece):
        for x, cell in enumerate(row):
            if cell:
                if (
                        piece_x + x < 0
                        or piece_x + x >= 10
                        or piece_y + y >= 20
                        or board[piece_y + y][piece_x + x]
                ):
                    return False
    return True

def place_piece():
    global board
    for y, row in enumerate(current_piece):
        for x, cell in enumerate(row):
            if cell:
                board[piece_y + y][piece_x + x] = current_piece_color

def draw_game_over():
    font = pygame.font.Font(None, 74)
    text = font.render('Game Over', True, RED)
    SCREEN.blit(text, (WIDTH // 4, HEIGHT // 2))

# Game loop
clock = pygame.time.Clock()
new_piece()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left()
            elif event.key == pygame.K_RIGHT:
                move_right()
            elif event.key == pygame.K_DOWN:
                move_down()
            elif event.key == pygame.K_UP:
                rotate_piece()

    if not game_over:
        move_down()

    SCREEN.fill(BLACK)
    draw_board()
    if not game_over:
        draw_piece()
    else:
        draw_game_over()
    pygame.display.flip()
    clock.tick(5)

pygame.quit()

