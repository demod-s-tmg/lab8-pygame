import pygame
import random
import math
from typing import List

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
NUM_SQUARES = 20
MIN_SIZE = 10
MAX_SIZE = 50
GLOBAL_MAX_SPEED = 4.0
V_MAX = GLOBAL_MAX_SPEED
V_MIN = 1.0
JITTER_PROBABILITY = 0.04
MAX_JITTER_ANGLE = 0.12

FLEE_RADIUS = 60

# Added a slightly larger radius for the chase behavior.
CHASE_RADIUS = 90

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

        # Record the exact time this square was created.
        self.birth_time: int = pygame.time.get_ticks()
        # Random lifespan between 30 and 180 seconds, converted to milliseconds.
        self.lifespan: float = random.uniform(30.0, 180.0) * 1000

        # Duplicated the flee pattern but reversed the logic to chase smaller squares

    def chase(self, others: List["Square"]):
        chase_vx = 0
        chase_vy = 0
        count = 0

        center_x = self.x + self.size / 2
        center_y = self.y + self.size / 2

        for other in others:
            if other is self:
                continue

            # Check if I am bigger than the other square
            if self.size > other.size:
                other_center_x = other.x + other.size / 2
                other_center_y = other.y + other.size / 2

                # Calculate vector TOWARDS the other square
                dx = other_center_x - center_x
                dy = other_center_y - center_y
                dist = math.hypot(dx, dy)

                if 0 < dist < CHASE_RADIUS:
                    chase_vx += dx / dist
                    chase_vy += dy / dist
                    count += 1

        # If we found prey, update our velocity towards them
        if count > 0:
            mag = math.hypot(chase_vx, chase_vy)
            if mag > 0:
                self.vx = (chase_vx / mag) * self.max_speed
                self.vy = (chase_vy / mag) * self.max_speed

    def flee(self, others: List["Square"]):
        flee_vx = 0
        flee_vy = 0
        count = 0

        center_x = self.x + self.size / 2
        center_y = self.y + self.size / 2

        for other in others:
            if other is self:
                continue

            if other.size > self.size:
                other_center_x = other.x + other.size / 2
                other_center_y = other.y + other.size / 2

                dx = center_x - other_center_x
                dy = center_y - other_center_y
                dist = math.hypot(dx, dy)

                if 0 < dist < FLEE_RADIUS:
                    flee_vx += dx / dist
                    flee_vy += dy / dist
                    count += 1

        if count > 0:
            mag = math.hypot(flee_vx, flee_vy)
            if mag > 0:
                self.vx = (flee_vx / mag) * self.max_speed
                self.vy = (flee_vy / mag) * self.max_speed

    def update(self):
        if random.random() < JITTER_PROBABILITY:
            current_angle = math.atan2(self.vy, self.vx)
            jitter = random.uniform(-MAX_JITTER_ANGLE, MAX_JITTER_ANGLE)
            new_angle = current_angle + jitter

            speed = min(math.hypot(self.vx, self.vy), self.max_speed)
            self.vx = math.cos(new_angle) * speed
            self.vy = math.sin(new_angle) * speed

        self.x += self.vx
        self.y += self.vy

        # Screen Wrapping instead of Hard Boundaries to prevent wall pinning
        if self.x < -self.size:
            self.x = SCREEN_WIDTH
        elif self.x > SCREEN_WIDTH:
            self.x = -self.size

        if self.y < -self.size:
            self.y = SCREEN_HEIGHT
        elif self.y > SCREEN_HEIGHT:
            self.y = -self.size

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
    pygame.display.set_caption("LAB 11 - Moving Squares Part IV")
    clock = pygame.time.Clock()
    squares = create_squares(NUM_SQUARES)

    font = pygame.font.SysFont("Arial", 20, bold=True)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        current_time = pygame.time.get_ticks()

        for i in range(len(squares)):
            if current_time - squares[i].birth_time > squares[i].lifespan:
                size = random.uniform(MIN_SIZE, MAX_SIZE)
                random_x = random.uniform(0, SCREEN_WIDTH - size)
                random_y = random.uniform(0, SCREEN_HEIGHT - size)

                squares[i] = Square(random_x, random_y, size)

        for square in squares:
            square.chase(squares)
            square.flee(squares)
            square.update()
            square.draw(screen)

        fps_text = font.render(f"FPS: {int(clock.get_fps())}", True, (0, 0, 0))
        screen.blit(fps_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
