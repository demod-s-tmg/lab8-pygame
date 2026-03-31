import pygame
import random
from typing import List

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
NUM_SQUARES = 10
SQUARE_SIZE = 30
BACKGROUND_COLOR = (255, 255, 255)  # White
FPS = 60


class Square:
    """Represents a square that moves around the screen."""

    def __init__(self, x: float, y: float, vx: float, vy: float):
        """Initialize a square."""
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        # Random color for each square
        self.color = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255),
        )

    def update(self):
        """Update the square's position and handle boundary bouncing."""
        # 1. Update position based on velocity
        self.x += self.vx
        self.y += self.vy

        # 2. Handle horizontal boundary bouncing
        # Check if hitting left (0) or right (SCREEN_WIDTH)
        if self.x <= 0 or self.x + SQUARE_SIZE >= SCREEN_WIDTH:
            self.vx *= -1  # Reverse x velocity

        # 3. Handle vertical boundary bouncing
        # Check if hitting top (0) or bottom (SCREEN_HEIGHT)
        if self.y <= 0 or self.y + SQUARE_SIZE >= SCREEN_HEIGHT:
            self.vy *= -1  # Reverse y velocity

    def draw(self, screen):
        """Draw the square on the screen."""
        pygame.draw.rect(screen, self.color, (self.x, self.y, SQUARE_SIZE, SQUARE_SIZE))


def create_squares(num: int) -> List[Square]:
    """Create a list of squares with random positions and velocities."""
    squares_list = []

    for _ in range(num):
        # Ensure the square starts fully inside the screen bounds
        random_x = random.uniform(0, SCREEN_WIDTH - SQUARE_SIZE)
        random_y = random.uniform(0, SCREEN_HEIGHT - SQUARE_SIZE)

        # Generate velocities between -4 and 4, avoiding 0 so they don't get stuck
        random_vx = random.uniform(-4, 4)
        random_vy = random.uniform(-4, 4)

        # Create the object and add to list
        new_square = Square(random_x, random_y, random_vx, random_vy)
        squares_list.append(new_square)

    return squares_list


def main():
    """Main game loop."""

    # Create the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Moving Squares - Lab 8")

    # Create clock for FPS control
    clock = pygame.time.Clock()

    # Create squares
    squares = create_squares(NUM_SQUARES)

    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update
        for square in squares:
            square.update()

        # Draw
        screen.fill(BACKGROUND_COLOR)
        for square in squares:
            square.draw(screen)

        # Update display and control FPS
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
