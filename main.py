from pathlib import Path
import pygame

# Constants
WIDTH, HEIGHT = 600, 800
CAR_DIMENSIONS = (50, 75)
BALL_DIMENSIONS = (50, 50)
FIELD_COLOUR = (0, 128, 0)
FPS = 30

# Accessing and scaling asset images
ASSETS_PATH = Path('Assets')
RED_CAR_FILE = "red_car.png"
WHITE_CAR_FILE = "white_car.png"
BALL_FILE = "basket-ball.png"

RED_CAR_IMAGE = pygame.image.load(ASSETS_PATH / RED_CAR_FILE)
RED_CAR = pygame.transform.scale(RED_CAR_IMAGE, CAR_DIMENSIONS)

WHITE_CAR_IMAGE = pygame.image.load(ASSETS_PATH / WHITE_CAR_FILE)
WHITE_CAR = pygame.transform.scale(WHITE_CAR_IMAGE, CAR_DIMENSIONS)
WHITE_CAR = pygame.transform.rotate(WHITE_CAR, 180)

BALL_IMAGE = pygame.image.load(ASSETS_PATH / BALL_FILE)
BALL = pygame.transform.scale(BALL_IMAGE, BALL_DIMENSIONS)


# Creating window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rocket League")


def draw_window(red_rect, white_rect, ball_rect):
    WIN.fill(FIELD_COLOUR)
    WIN.blit(RED_CAR, (red_rect.x, red_rect.y))
    WIN.blit(WHITE_CAR, (white_rect.x, white_rect.y))
    WIN.blit(BALL, (ball_rect.x, ball_rect.y))
    pygame.display.update()


def main():
    red_rect = pygame.Rect(WIDTH // 2 - CAR_DIMENSIONS[0] // 2, 650, CAR_DIMENSIONS[0], CAR_DIMENSIONS[1])
    white_rect = pygame.Rect(WIDTH // 2 - CAR_DIMENSIONS[0] // 2, 150 - CAR_DIMENSIONS[1], CAR_DIMENSIONS[0], CAR_DIMENSIONS[1])
    ball_rect = pygame.Rect(WIDTH // 2 - BALL_DIMENSIONS[0] // 2, HEIGHT // 2 - BALL_DIMENSIONS[1] // 2, BALL_DIMENSIONS[0], BALL_DIMENSIONS[1])
    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        ball_rect.y += -1
        draw_window(red_rect, white_rect, ball_rect)

    pygame.quit()


if __name__ == '__main__':
    main()
