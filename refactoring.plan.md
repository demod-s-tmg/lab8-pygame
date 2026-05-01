# 1. Overview

This project is a small Pygame simulation where colored squares move on screen, chase smaller squares, flee larger squares, and respawn after a random lifespan. The core runtime behavior is centralized in `main.py`, mainly through the `Square` class (`chase`, `flee`, `update`, `draw`) and the main game loop.

The code is already functional and readable for a first-year level, but it can be improved with light refactoring in three areas:
- Reduce repeated logic (especially center and respawn calculations).
- Improve naming clarity and function boundaries in the main loop.
- Keep behavior-focused comments consistent and beginner-friendly.

The goal is to keep the same behavior and structure, while making the code easier to read, explain, and maintain.

# 2. Refactoring Goals

- Improve readability with clearer names for intermediate values and helper functions.
- Reduce duplication by extracting tiny helper methods for repeated calculations.
- Keep behavior unchanged (same simulation rules, timing, rendering, and controls).
- Make intent explicit with concise inline comments in the final code.
- Keep the refactoring incremental and safe for beginners.

# 3. Step-by-Step Refactoring Plan

## Step 1: Add tiny helper methods for repeated center-point math in `Square`

What to do:
- In `Square`, add a small helper like `get_center(self) -> tuple[float, float]` (or equivalent typing supported by the current Python version).
- Replace repeated `self.x + self.size / 2` and `self.y + self.size / 2` usages in `chase` and `flee` with this helper.

Why this helps:
- The same formula appears many times; extracting it reduces copy-paste mistakes.
- It clarifies intent: this operation means “square center,” not just arithmetic.

Inline-comment instruction for final refactored code:
- Add a short inline comment near the helper explaining what changed (center calculation extracted) and why (less duplication, clearer intent).
- Add a short comment where the helper is used to reinforce the concept of “single source of truth” for repeated logic.

Optional before/after sketch:

Before:
```python
center_x = self.x + self.size / 2
center_y = self.y + self.size / 2
```

After:
```python
center_x, center_y = self.get_center()  # Reuse one center formula everywhere.
```

## Step 2: Extract square creation details into a small helper function

What to do:
- Create a helper function (for example `create_random_square() -> Square`) that:
  - Picks random size.
  - Picks valid random position based on that size.
  - Returns a new `Square`.
- Use this helper both in `create_squares` and in the respawn section inside `main`.

Why this helps:
- Random square generation is currently duplicated in two places.
- A dedicated helper makes future rule changes (size range, spawn bounds) safer and easier.

Inline-comment instruction for final refactored code:
- Add a concise comment near the helper explaining what changed (spawn logic centralized) and why (avoid inconsistencies).
- Add a concise comment at one call site linking the change to maintainability.

Optional before/after sketch:

Before:
```python
size = random.uniform(MIN_SIZE, MAX_SIZE)
random_x = random.uniform(0, SCREEN_WIDTH - size)
random_y = random.uniform(0, SCREEN_HEIGHT - size)
squares[i] = Square(random_x, random_y, size)
```

After:
```python
squares[i] = create_random_square()  # One helper controls all spawn rules.
```

## Step 3: Give the time-based respawn condition a clear helper name

What to do:
- Add a tiny method in `Square`, such as `is_expired(current_time: int) -> bool`, returning whether lifespan is exceeded.
- Replace direct lifespan checks in `main` with that method.

Why this helps:
- The condition is conceptually meaningful; naming it makes code read like English.
- It keeps lifespan rules encapsulated with square state.

Inline-comment instruction for final refactored code:
- Add a concise comment near `is_expired` explaining what changed (condition wrapped in method) and why (better readability and encapsulation).
- Mention the concept of encapsulation in simple terms.

Optional before/after sketch:

Before:
```python
if current_time - squares[i].birth_time > squares[i].lifespan:
```

After:
```python
if squares[i].is_expired(current_time):  # Ask the object about its own state.
```

## Step 4: Make main-loop stages visually explicit with micro-functions

What to do:
- Extract tiny free functions (or local functions) for major loop stages, for example:
  - `handle_events() -> bool` (returns running state)
  - `respawn_expired_squares(squares, current_time)`
  - `apply_square_behaviors(squares)`
  - `update_and_draw_squares(squares, dt, screen)`
- Keep each function short and behavior-preserving.

Why this helps:
- Beginners can understand the frame lifecycle as named steps.
- It becomes easier to test or discuss one stage at a time.

Inline-comment instruction for final refactored code:
- Add one concise comment above each extracted function: what stage it represents and why splitting stages improves readability.
- Keep comments short and focused on intent, not obvious syntax.

Optional before/after sketch:

Before:
```python
for square in squares:
    square.chase(squares)
    square.flee(squares)

for square in squares:
    square.update(dt)
    square.draw(screen)
```

After:
```python
apply_square_behaviors(squares)  # Decision stage
update_and_draw_squares(squares, dt, screen)  # Movement + rendering stage
```

## Step 5: Light naming cleanup for intermediate vectors and counters

What to do:
- In `chase` and `flee`, rename temporary variables to emphasize meaning, for example:
  - `count` -> `nearby_targets` / `nearby_threats`
  - `mag` -> `direction_magnitude`
- Keep logic unchanged.

Why this helps:
- More descriptive names reduce mental effort for readers.
- It supports debugging because variable intent is explicit.

Inline-comment instruction for final refactored code:
- Add concise comments only where a rename carries conceptual value (for example, why normalized direction is used).
- Mention “readability through naming” as a beginner concept.

## Step 6: Keep and standardize concise explanatory inline comments

What to do:
- Review existing comments and keep the useful intent-level ones.
- Add or adjust comments so each important refactor includes:
  - What changed.
  - Why the change improves readability/maintainability/correctness.
  - A short programming concept note (e.g., encapsulation, DRY, single responsibility).
- Remove comments that are purely obvious or noisy.

Why this helps:
- Students can connect code structure to engineering reasoning.
- Comments become a learning aid rather than clutter.

Inline-comment instruction for final refactored code:
- Ensure each newly refactored area has at least one concise inline comment covering what/why/concept.
- Keep each comment short enough to read quickly in class.

# 4. Final Output Requirements (Mandatory)

When this plan is executed, the output MUST:
- Contain only the refactored code.
- Preserve current behavior (movement, chase/flee logic, respawn timing, rendering, FPS display, quit handling).
- Include concise inline comments that explicitly explain:
  - What changed.
  - Why it improves the code.
  - Relevant programming concepts (for beginners).
- Keep comments beginner-friendly and not overly verbose.
- Avoid advanced patterns or heavy abstractions.

# 5. Key Concepts for Students

- DRY (Don’t Repeat Yourself): Put repeated logic in one helper to reduce bugs.
- Encapsulation: Let an object answer questions about its own state (`is_expired`).
- Separation of responsibilities: Split large loops into small named stages.
- Readability through naming: Better temporary names make logic easier to follow.
- Behavior preservation: Refactoring changes structure, not program results.

# 6. Safety Notes

- Refactor in very small steps; run the program after each step.
- Keep one behavior check list while testing: square movement, chase/flee reactions, respawn, wraparound, FPS text, window close.
- Avoid changing constants during refactor; only move/rename logic first.
- If a step causes unexpected behavior, revert just that step and retry with smaller edits.
- Keep comments concise and accurate; update comments whenever code intent changes.