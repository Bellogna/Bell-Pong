# Bell Pong

A classic 2-player Pong game built from scratch with Python and Pygame.
Press **Enter** to start — first player to **5 points** wins, then press
**Enter** again for a rematch.

Project 1 in my learn-to-code portfolio: I'm recreating classic games to
learn programming fundamentals while working toward a career in IT support.

## How to run

You need Python 3 installed, then:

```bash
pip install pygame-ce
python pong.py
```

> Note: this installs Pygame Community Edition (`pygame-ce`), a drop-in
> replacement that still imports as `pygame`. It's used here because the
> original `pygame` package doesn't ship an install for Python 3.14+ yet.

## Controls

| Player | Up | Down |
|---|---|---|
| Left paddle | `W` | `S` |
| Right paddle | `↑` | `↓` |

**Enter** starts the game / starts a rematch. **Esc** or closing the window quits.
The ball resets to the center after each point, and the score is shown at the top.

## What I learned building this

- Variables for game settings, scores, and game state (`game_started`, `winner`)
- The game loop: read input → update positions → draw, at 60 FPS
- Rectangles, screen coordinates, and collision detection (`colliderect`)
- Keyboard input and `if` statements — including how much indentation matters in Python
- Bouncing by reversing a speed's sign, scoring, and ball resets
- Text rendering, and centering text with `get_rect(center=...)`
- Debugging: install/version issues, autocomplete surprises, and syntax errors

## What's next

- [ ] Ball speeds up a little on each paddle hit
- [ ] Single-player mode with a simple computer opponent
- [ ] Sound effects on bounce and score
