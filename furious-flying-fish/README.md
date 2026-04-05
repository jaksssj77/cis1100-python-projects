# Furious Flying Fish

An interactive projectile-based game built in Python using object-oriented design.

## Features
- Mouse-controlled launching system
- Physics-based motion (velocity + gravity)
- Collision detection between fish and targets
- Game state management (win/lose conditions)

## Structure
- `arena.py`: manages game state and interactions
- `fish.py`: handles fish movement and collisions
- `target.py`: represents moving targets
- `furious_fish.py`: main game loop


## How to Run
Requires a level file (e.g. `target_file.txt`):

```bash
python furious_fish.py target_file.txt
```
