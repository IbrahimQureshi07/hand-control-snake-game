# Hand-Control Snake Game

Desktop Snake game with **optional hand tracking** (webcam + MediaPipe) or **keyboard** (arrow keys). Built with Python, Tkinter, OpenCV, and MediaPipe Tasks API.

## Project layout

```
├── src/                    # Main game code
│   ├── snake_game_tkinter.py   # Recommended: Tkinter + hand or keyboard
│   └── snake_game.py           # Optional: Pygame + keyboard
├── tools/                  # Camera utilities (optional)
│   ├── test_camera.py
│   └── check_camera_detailed.py
├── models/                 # Auto-downloaded on first run (gitignored)
│   └── hand_landmarker.task
├── requirements.txt
└── README.md
```

## Setup

```bash
pip install -r requirements.txt
```

Hand mode downloads `hand_landmarker.task` into `models/` on first run (internet required once).

## Run

From the project root:

```bash
python src/snake_game_tkinter.py
```

**Pygame variant** (install pygame first):

```bash
pip install pygame
python src/snake_game.py
```

**Test camera only:**

```bash
python tools/test_camera.py
```

## Controls

- **Hand mode** (default in `snake_game_tkinter.py`): point your index finger — see in-file `CONTROL_MODE`.
- **Keyboard**: arrow keys; **R** to restart after game over.
- Windows: allow **desktop apps** to use the camera in **Settings → Privacy → Camera**.

## Requirements

- Python 3.10+
- Webcam for hand mode
