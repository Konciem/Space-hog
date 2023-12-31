import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT =1000, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Hog")

color = (18, 31 ,148)
WIN.fill(color)
pygame.display.flip()

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5

FONT = pygame.font.SysFont("Arial", 30)

def draw(player, elapsed_time):

    pygame.draw.rect(WIN, "red", player)

    time_text = FONT.render(f"Time: {(round(elapsed_time))}s", 1, "white")

    pygame.display.update()
def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT,
                         PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()

    start_time = time.time()
    elapsed_time = 0

    while run:

        clock.tick(60)
        elapsed_time = time.time() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                print(f'dupa')
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
            WIN.fill(color)
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
            WIN.fill(color)

        draw(player, elapsed_time)

    pygame.quit()

if __name__ == "__main__":
    main()

