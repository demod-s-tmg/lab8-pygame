# lab8-pygame

An interactive Pygame simulation demonstrating emergent behavior through inverse linear interpolation and flocking-style flee mechanics.

## Overview

This project creates 20 colored squares on a 800×600 canvas, each with dynamically computed properties:
- **Size**: Random between 10–50 pixels
- **Speed**: Inverse to size (larger squares are slower)
- **Direction**: Random movement with probabilistic jitter
- **Flee Behavior**: Smaller squares flee from nearby larger squares within a 60-pixel radius

The squares bounce off screen edges and update their collective velocities each frame based on flee pressures.

## Features

- **Inverse Linear Interpolation**: Speed scales inversely with square size; larger squares move slower (max 4.0 units/frame)
- **Jitter**: 4% chance per frame for each square to randomly shift its direction by up to ±0.12 radians
- **Flee Mechanic**: Smaller squares detect and move away from larger threats within FLEE_RADIUS
- **Collision-Free Edge Handling**: Squares clamp to screen bounds and bounce reversibly

## Setup (Windows PowerShell)

1. Create the virtual environment:
   ```powershell
   python -m venv .venv
   ```
2. Activate it:
   ```powershell
   . .\.venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

## Run

```powershell
python main.py
```

## Configuration

All simulation parameters are configurable at the top of `main.py`:
- `NUM_SQUARES`: Number of squares (default: 20)
- `MIN_SIZE`, `MAX_SIZE`: Square size range (default: 10–50)
- `GLOBAL_MAX_SPEED`: Maximum velocity cap (default: 4.0)
- `FLEE_RADIUS`: Detection radius for flee behavior (default: 60)
- `JITTER_PROBABILITY`: Chance of direction shift per frame (default: 0.04)
- `MAX_JITTER_ANGLE`: Magnitude of direction jitter in radians (default: 0.12)

## Requirements

- Python 3.8+
- pygame 2.6.1
