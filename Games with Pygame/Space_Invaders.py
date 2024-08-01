import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_WIDTH = 60
PLAYER_HEIGHT = 15
ENEMY_WIDTH = 50
ENEMY_HEIGHT = 30
BULLET_WIDTH = 5
BULLET_HEIGHT = 10
ENEMY_COUNT = 5
PLAYER_SPEED = 5
ENEMY_SPEED = 3
BULLET_SPEED = 7
FPS = 60

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

# Font setup
font = pygame.font.SysFont(None, 55)


# Player class
class Player:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2
        self.y = SCREEN_HEIGHT - PLAYER_HEIGHT - 10
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.color = GREEN
        self.speed = PLAYER_SPEED

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self, dx):
        self.x += dx
        self.x = max(0, min(SCREEN_WIDTH - self.width, self.x))


# Enemy class
class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = ENEMY_WIDTH
        self.height = ENEMY_HEIGHT
        self.color = RED
        self.speed = ENEMY_SPEED
        self.direction = 1

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        self.x += self.speed * self.direction
        if self.x <= 0 or self.x >= SCREEN_WIDTH - self.width:
            self.direction *= -1
            self.y += self.height


# Bullet class
class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = BULLET_WIDTH
        self.height = BULLET_HEIGHT
        self.color = BLUE

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        self.y -= BULLET_SPEED


def display_message(message, color):
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)


def main():
    clock = pygame.time.Clock()
    running = True
    game_over = False
    game_won = False

    player = Player()
    enemies = [Enemy(random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH), random.randint(0, 100)) for _ in range(ENEMY_COUNT)]
    bullets = []

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if not game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.move(-player.speed)
            if keys[pygame.K_RIGHT]:
                player.move(player.speed)
            if keys[pygame.K_SPACE]:
                bullets.append(Bullet(player.x + player.width // 2 - BULLET_WIDTH // 2, player.y))

            for bullet in bullets[:]:
                bullet.move()
                if bullet.y < 0:
                    bullets.remove(bullet)

            for enemy in enemies[:]:
                enemy.move()
                if enemy.y >= SCREEN_HEIGHT - ENEMY_HEIGHT:
                    game_over = True
                    break

            for bullet in bullets[:]:
                for enemy in enemies[:]:
                    if (bullet.x < enemy.x + enemy.width and
                            bullet.x + bullet.width > enemy.x and
                            bullet.y < enemy.y + enemy.height and
                            bullet.y + bullet.height > enemy.y):
                        bullets.remove(bullet)
                        enemies.remove(enemy)
                        break

            if len(enemies) == 0:
                game_won = True
                game_over = True

            player.draw()
            for enemy in enemies:
                enemy.draw()
            for bullet in bullets:
                bullet.draw()

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
