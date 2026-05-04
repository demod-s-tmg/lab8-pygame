for qn 1.
Instead of one loop, we likely need a sequence of operations or multiple loops one for each specific batch of squares. Instead of relying entirely on create_random_square() (which enforces randomness).look at how a square is actually built. If we look at the Square class __init__, we can create a square by passing specific x, y, and size parameters directly (e.g., Square(random_x, random_y, specific_size)).  we will need to ensure that the x and y coordinates are still generated safely within the screen bounds for these new, fixed-size squares, just like the original helper function does 

for qn 2.
instead of using the old squares[i] = create_random_square(), i use squares[i] = create_fixed_square(old_size) this way When square die, they are re-spawn with the same size. instead of a random square.

for qn3.
during the class i did this exercise and to fix the squares getting stuck on the walls, i decided to completely replace the hard bounce boundary logic inside update() with "screen wrapping". now, if self.x < -self.size, i teleport it to SCREEN_WIDTH, and vice versa. this completely stopped the wall pinning bug because there are no solid walls to get stuck on anymore.

for qn 4.
for this exercise i used Pygame's built-in colliderect method by temporarily creating pygame.Rect objects for the check

for qn5.
for this exercise, i implimented a nested loop to check every square against every other square in the list. i used the check_collision method from exercise 4 to detect overlaps. once a collision is confirmed, i check if the predator square's size is greater than the prey square's size. if it is, the smaller square is considered "eaten" and is immediately replaced by a newly spawned square using the create_fixed_square(old_size) helper, ensuring it respawns with its exact original size.

for qn6. 
for this exercise, i made the predator grow proportionally by calculating the area of both squares, adding them together, and then getting the square root to find the new width

for qn7.
for this exercise, i added a self.history list to the square class that appends the get_center() coordinates every frame inside the update loop. i used pop(0) to ensure the list length never exceeds TRAILS_LENGTH (30). and if dist < SCREEN_WIDTH / 2: it cut the lines into half.