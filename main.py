import pygame
import random
import math
from typing import List

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
NUM_SQUARES = 100
MIN_SIZE = 10
MAX_SIZE = 50
GLOBAL_MAX_SPEED = 4.0
V_MAX = GLOBAL_MAX_SPEED
V_MIN = 1.0

BACKGROUND_COLOR = (255, 255, 255)
FPS = 60


class Square:
    def __init__(self, x: float, y: float, size: float):
        self.x = x
        self.y = y
        self.size = size

        t = (self.size - MIN_SIZE) / (MAX_SIZE - MIN_SIZE)

        computed_speed = V_MAX - t * (V_MAX - V_MIN)
        self.max_speed = min(computed_speed, GLOBAL_MAX_SPEED)

        angle = random.uniform(0, 2 * math.pi)
        self.vx = math.cos(angle) * self.max_speed
        self.vy = math.sin(angle) * self.max_speed

        self.color = (
            random.randint(50, 200),
            random.randint(50, 200),
            random.randint(50, 200),
        )

    def update(self):
        self.x += self.vx
        self.y += self.vy

        if self.x <= 0 or self.x + self.size >= SCREEN_WIDTH:
            self.vx *= -1
        if self.y <= 0 or self.y + self.size >= SCREEN_HEIGHT:
            self.vy *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))


def create_squares(num: int) -> List[Square]:
    squares_list = []
    for _ in range(num):
        size = random.uniform(MIN_SIZE, MAX_SIZE)
        random_x = random.uniform(0, SCREEN_WIDTH - size)
        random_y = random.uniform(0, SCREEN_HEIGHT - size)

        new_square = Square(random_x, random_y, size)
        squares_list.append(new_square)
    return squares_list


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("EPITA Lab - Inverse Linear Interpolation")
    clock = pygame.time.Clock()
    squares = create_squares(NUM_SQUARES)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        for square in squares:
            square.update()
            square.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
