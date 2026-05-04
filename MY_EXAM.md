for qn 1.
Instead of one loop, we likely need a sequence of operations or multiple loops one for each specific batch of squares. Instead of relying entirely on create_random_square() (which enforces randomness).look at how a square is actually built. If we look at the Square class __init__, we can create a square by passing specific x, y, and size parameters directly (e.g., Square(random_x, random_y, specific_size)).  we will need to ensure that the x and y coordinates are still generated safely within the screen bounds for these new, fixed-size squares, just like the original helper function does 

for qn 2.
instead of using the old squares[i] = create_random_square(), i use squares[i] = create_fixed_square(old_size) this way When square die, they are re-spawn with the same size. instead of a random square.

for qn3.
during the class i did this exercise and to fix the squares getting stuck on the walls, i decided to completely replace the hard bounce boundary logic inside update() with "screen wrapping". now, if self.x < -self.size, i teleport it to SCREEN_WIDTH, and vice versa. this completely stopped the wall pinning bug because there are no solid walls to get stuck on anymore.

for qn 4.
for this exercise i used Pygame's built-in colliderect method by temporarily creating pygame.Rect objects for the check

for qn5.
