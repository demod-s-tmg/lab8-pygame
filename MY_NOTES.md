# My Notes
understandings:

i wanted to make the 100 squares feel more natural, so i worked on linking their size to their speed and adding a "jitter" effect . the core idea was that bigger squares should be heavier and slower while smaller ones should be fast, which i handled using inverse linear interpolation . i also learned that to change a square's direction without changing its speed, i had to use a rigid transform rotation by shifting the angle of the velocity vector using trigonometry.

decsions:

the math and mapping: i picked a random size between 10 and 50 for each square and mapped it to a 0-to-1 ratio t using the formula t=(size−10)/(50−10) . i then calculated computed_speed so that the smallest squares hit the GLOBAL_MAX_SPEED of 4.0, and the largest move at 1.0. i used a min() check to make sure the global speed cap is strictly enforced even if the math tries to go higher.

jitter implementation: i set a JITTER_PROBABILITY of 0.04 (about a 4% chance per frame) so the direction changes feel occasional rather than constant vibration . i used math.atan2 to find the current heading, added a small random angle of up to 0.12 radians, and rebuilt the vx and vy using math.cos and math.sin to keep the magnitude the same.

code safety: i made sure the code is defensive by using math.hypot to re-verify the speed during jitter and checking that no square spawns outside the 800x600 screen bounds . i also used explicit boundary checks for the left, right, top, and bottom to make sure the squares bounce correctly using their specific size attribute.

questions:

it was interesting to see how rotation alone shouldn't actually change the speed, but adding that min(math.hypot(self.vx, self.vy), self.max_speed) guard path is a good way to prevent numerical drift errors over long runs.

i realized that using a class for the squares made it much easier to manage all these new attributes like size and max_speed compared to the dictionary method mentioned earlier in the lab.

the visual feedback of seeing 100 squares with different speeds and slight random turns makes the whole app feel way more like a real simulation and less like a basic loop.