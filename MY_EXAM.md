for qn 1.
Instead of one loop, we likely need a sequence of operations or multiple loops one for each specific batch of squares. Instead of relying entirely on create_random_square() (which enforces randomness).look at how a square is actually built. If we look at the Square class __init__, we can create a square by passing specific x, y, and size parameters directly (e.g., Square(random_x, random_y, specific_size)).  we will need to ensure that the x and y coordinates are still generated safely within the screen bounds for these new, fixed-size squares, just like the original helper function does 

for qn 2.
instead of using the old squares[i] = create_random_square(), i use squares[i] = create_fixed_square(old_size) this way When square die, they are re-spawn with the same size. instead of a random square.

for qn 3. 