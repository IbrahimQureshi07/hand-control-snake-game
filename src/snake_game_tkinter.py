import math
import tkinter as tk
import random
import time
import urllib.request
from collections import Counter, deque
from pathlib import Path

# Hand control imports (only needed when CONTROL_MODE = 'hand')
# MediaPipe 0.10+ uses the Tasks API only (mp.solutions was removed from the wheel).
try:
    import cv2
    import mediapipe as mp
    _ = mp.tasks.vision.HandLandmarker
    HAND_CONTROL_AVAILABLE = True
except ImportError:
    HAND_CONTROL_AVAILABLE = False
    print("Note: OpenCV or MediaPipe not installed. Hand control won't work.")
    print("Install with: pip install opencv-python mediapipe")

# Bundled / cached model (downloaded once into project folder)
HAND_MODEL_URL = (
    "https://storage.googleapis.com/mediapipe-models/hand_landmarker/"
    "hand_landmarker/float16/1/hand_landmarker.task"
)


def ensure_hand_landmarker_model() -> Path:
    """Download Google's hand_landmarker.task if missing (one-time, ~few MB)."""
    # Repo root /models (this file lives in /src)
    model_dir = Path(__file__).resolve().parent.parent / "models"
    model_dir.mkdir(parents=True, exist_ok=True)
    path = model_dir / "hand_landmarker.task"
    if path.is_file() and path.stat().st_size > 100_000:
        return path
    print("Downloading Hand Landmarker model (first run only)...")
    urllib.request.urlretrieve(HAND_MODEL_URL, path)
    return path

# ============================================
# CONTROL MODE SETTING - YAHAN CHANGE KARO
# ============================================
# Line 8 par CONTROL_MODE change karo:
# 'keyboard' = Arrow keys se khelo (abhi ke liye)
# 'hand' = Hand gestures se khelo (baad mein camera ke saath)
CONTROL_MODE = 'hand'  # YAHAN 'keyboard' ya 'hand' likho

# ============================================
# GAME SETTINGS
# ============================================
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# Colors
BLACK = '#000000'
GREEN = '#00FF00'
RED = '#FF0000'
WHITE = '#FFFFFF'
DARK_GREEN = '#00C800'
BLUE = '#0000FF'

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Hand control tuning (index MCP → tip vector, normalized 0–1 coords)
HAND_MIN_POINT_NORM = 0.028  # ignore tiny / collapsed finger poses
HAND_SMOOTH_MAXLEN = 3       # majority over last N frames reduces jitter

def _direction_from_pointing_vector(dx: float, dy: float):
    """
    Map pointing vector (index MCP → tip) to UP/DOWN/LEFT/RIGHT using atan2 sectors.
    Uses equal 90° quadrants so left/right feel symmetric vs axis-only thresholds.
    """
    if math.hypot(dx, dy) < HAND_MIN_POINT_NORM:
        return None
    a = math.atan2(dy, dx)
    if -math.pi / 4 <= a <= math.pi / 4:
        return RIGHT
    if math.pi / 4 < a < 3 * math.pi / 4:
        return DOWN
    if a >= 3 * math.pi / 4 or a <= -3 * math.pi / 4:
        return LEFT
    return UP


def _smooth_hand_direction(buffer: deque, raw):
    """Majority of recent non-None readings; tie → latest (responsive)."""
    buffer.append(raw)
    vals = [d for d in buffer if d is not None]
    if not vals:
        return None
    if len(vals) == 1:
        return vals[0]
    best, cnt = Counter(vals).most_common(1)[0]
    if cnt >= 2:
        return best
    return vals[-1]

class Snake:
    def __init__(self):
        self.length = 3
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = RIGHT
        self.score = 0
        
        # Initialize snake body
        for i in range(1, self.length):
            self.positions.append((self.positions[0][0] - i, self.positions[0][1]))
    
    def get_head_position(self):
        return self.positions[0]
    
    def update(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = ((cur[0] + x) % GRID_WIDTH, (cur[1] + y) % GRID_HEIGHT)
        
        if len(self.positions) > 2 and new in self.positions[2:]:
            return False  # Game over - snake hit itself
        
        self.positions.insert(0, new)
        if len(self.positions) > self.length:
            self.positions.pop()
        
        return True
    
    def reset(self):
        self.length = 3
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = RIGHT
        self.score = 0
        for i in range(1, self.length):
            self.positions.append((self.positions[0][0] - i, self.positions[0][1]))

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.randomize_position()
    
    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

class Game:
    def __init__(self):
        global CONTROL_MODE  # Declare global at the start of method
        
        self.root = tk.Tk()
        self.root.title('Snake Game — Hand or Arrow Keys')
        self.root.resizable(False, False)
        
        # Canvas for drawing
        self.canvas = tk.Canvas(self.root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg=BLACK)
        self.canvas.pack()
        
        # Score label
        self.score_label = tk.Label(self.root, text='Score: 0', font=('Arial', 16), fg=WHITE, bg=BLACK)
        self.score_label.pack()
        
        # Mode label
        self.mode_label = tk.Label(self.root, text=f'Mode: {CONTROL_MODE.upper()}', font=('Arial', 12), fg=WHITE, bg=BLACK)
        self.mode_label.pack()
        
        # Hand detection status label (for hand mode)
        self.hand_status_label = None
        if CONTROL_MODE == 'hand':
            self.hand_status_label = tk.Label(self.root, text='Hand: Waiting...', font=('Arial', 10), fg='yellow', bg=BLACK)
            self.hand_status_label.pack()
        
        self.snake = Snake()
        self.food = Food()
        self.game_over = False
        
        # Bind keyboard events
        self.root.bind('<KeyPress-Up>', lambda e: self.change_direction(UP))
        self.root.bind('<KeyPress-Down>', lambda e: self.change_direction(DOWN))
        self.root.bind('<KeyPress-Left>', lambda e: self.change_direction(LEFT))
        self.root.bind('<KeyPress-Right>', lambda e: self.change_direction(RIGHT))
        self.root.bind('<KeyPress-r>', lambda e: self.restart_game())
        self.root.bind('<KeyPress-R>', lambda e: self.restart_game())
        self.root.focus_set()
        
        # For hand control (MediaPipe Tasks API + OpenCV)
        self.cap = None
        self.hand_landmarker = None
        self._hand_frame_ts_ms = 0
        self._hand_vote_buffer = deque(maxlen=HAND_SMOOTH_MAXLEN)
        
        if CONTROL_MODE == 'hand':
            if not self.init_hand_control():
                print("=" * 50)
                print("ERROR: Hand control initialization failed!")
                print("Switching to keyboard mode...")
                print("=" * 50)
                CONTROL_MODE = 'keyboard'  # global already declared at method start
                self.mode_label.config(text=f'Mode: {CONTROL_MODE.upper()}')
                if self.hand_status_label:
                    self.hand_status_label.destroy()
                    self.hand_status_label = None
    
    def init_hand_control(self):
        """Open default webcam and MediaPipe Hand Landmarker (Tasks API)."""
        if not HAND_CONTROL_AVAILABLE:
            print("ERROR: OpenCV or MediaPipe not installed!")
            print("Install with: pip install opencv-python mediapipe")
            return False
        
        try:
            print("=" * 50)
            print("Hand mode: opening webcam (built-in / USB)...")
            print("=" * 50)
            
            self.cap = self._open_first_working_camera()
            if self.cap is None or not self.cap.isOpened():
                print("ERROR: No working camera found. Try closing other apps using the camera.")
                print("Windows: Settings > Privacy > Camera > allow desktop apps.")
                return False
            
            model_path = str(ensure_hand_landmarker_model())
            BaseOptions = mp.tasks.BaseOptions
            HandLandmarker = mp.tasks.vision.HandLandmarker
            HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
            VisionRunningMode = mp.tasks.vision.RunningMode
            
            options = HandLandmarkerOptions(
                base_options=BaseOptions(model_asset_path=model_path),
                running_mode=VisionRunningMode.VIDEO,
                num_hands=1,
                min_hand_detection_confidence=0.5,
                min_hand_presence_confidence=0.45,
                min_tracking_confidence=0.45,
            )
            self.hand_landmarker = HandLandmarker.create_from_options(options)
            self._hand_frame_ts_ms = 0
            self._hand_vote_buffer.clear()
            
            print("Hand control initialized (MediaPipe Tasks + webcam).")
            print("- Point index finger (knuckle to tip) in the air — angle picks direction.")
            print("=" * 50)
            return True
        except Exception as e:
            print(f"ERROR initializing hand control: {e}")
            if self.cap is not None:
                self.cap.release()
                self.cap = None
            return False

    def _open_first_working_camera(self):
        """Try camera indices 0..3 with DirectShow on Windows, then default backend."""
        for idx in range(4):
            print(f"  Trying camera index {idx}...")
            for use_dshow in (True, False):
                if use_dshow:
                    cap = cv2.VideoCapture(idx, cv2.CAP_DSHOW)
                else:
                    cap = cv2.VideoCapture(idx)
                if not cap.isOpened():
                    cap.release()
                    continue
                cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
                # Warm up — some drivers return empty first frames
                good = None
                for _ in range(30):
                    ret, frame = cap.read()
                    if ret and frame is not None and frame.size > 0:
                        good = frame
                        break
                    time.sleep(0.03)
                if good is not None:
                    print(f"  [OK] Camera index {idx} — frame shape {good.shape}")
                    return cap
                cap.release()
        return None
    
    def get_hand_direction(self):
        """Index MCP → index tip vector, atan2 sectors, smoothed over recent frames."""
        if not HAND_CONTROL_AVAILABLE or self.cap is None or self.hand_landmarker is None:
            return None
        
        try:
            ret, frame = self.cap.read()
            if not ret or frame is None:
                raw = None
            else:
                frame = cv2.flip(frame, 1)
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                
                self._hand_frame_ts_ms += 33
                mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
                result = self.hand_landmarker.detect_for_video(mp_image, self._hand_frame_ts_ms)
                
                if not result.hand_landmarks:
                    raw = None
                else:
                    lm = result.hand_landmarks[0]
                    # INDEX_FINGER_MCP (5) → INDEX_FINGER_TIP (8): stable "pointing" direction
                    mcp = lm[5]
                    tip = lm[8]
                    dx = tip.x - mcp.x
                    dy = tip.y - mcp.y
                    raw = _direction_from_pointing_vector(dx, dy)
            
            return _smooth_hand_direction(self._hand_vote_buffer, raw)
        except Exception as e:
            print(f"Error in hand detection: {e}")
            return None
    
    def change_direction(self, new_direction):
        """Change snake direction if valid"""
        if self.game_over:
            return
        
        # Prevent reversing into itself
        if (new_direction == UP and self.snake.direction != DOWN) or \
           (new_direction == DOWN and self.snake.direction != UP) or \
           (new_direction == LEFT and self.snake.direction != RIGHT) or \
           (new_direction == RIGHT and self.snake.direction != LEFT):
            self.snake.direction = new_direction
    
    def handle_hand_input(self):
        """Handle hand gesture input"""
        if CONTROL_MODE == 'hand':
            direction = self.get_hand_direction()
            if direction:
                self.change_direction(direction)
                # Update status label
                if self.hand_status_label:
                    dir_name = ['UP', 'DOWN', 'LEFT', 'RIGHT'][[UP, DOWN, LEFT, RIGHT].index(direction)]
                    self.hand_status_label.config(text=f'Hand: Detected - {dir_name}', fg='green')
            else:
                # Update status label - no hand detected
                if self.hand_status_label:
                    self.hand_status_label.config(text='Hand: Not detected - Show hand to camera', fg='yellow')
    
    def restart_game(self):
        """Restart the game"""
        self.snake.reset()
        self.food.randomize_position()
        self.game_over = False
        self.score_label.config(text=f'Score: {self.snake.score}')
        self.canvas.delete('game_over')
    
    def update(self):
        """Update game state"""
        if not self.game_over:
            # Handle hand input if needed
            if CONTROL_MODE == 'hand':
                self.handle_hand_input()
            
            # Update snake
            if not self.snake.update():
                self.game_over = True
                self.canvas.create_text(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 20,
                                      text='GAME OVER!', fill=RED, font=('Arial', 36), tags='game_over')
                self.canvas.create_text(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20,
                                      text='Press R to Restart', fill=WHITE, font=('Arial', 16), tags='game_over')
            
            # Check if snake ate food
            if self.snake.get_head_position() == self.food.position:
                self.snake.length += 1
                self.snake.score += 10
                self.score_label.config(text=f'Score: {self.snake.score}')
                self.food.randomize_position()
                # Make sure food doesn't spawn on snake
                while self.food.position in self.snake.positions:
                    self.food.randomize_position()
        
        # Draw everything
        self.draw()
        
        # Schedule next update
        self.root.after(100, self.update)  # 100ms = 10 FPS
    
    def draw(self):
        """Draw game elements"""
        self.canvas.delete('snake')
        self.canvas.delete('food')
        
        # Draw snake
        for i, p in enumerate(self.snake.positions):
            x1 = p[0] * GRID_SIZE
            y1 = p[1] * GRID_SIZE
            x2 = x1 + GRID_SIZE
            y2 = y1 + GRID_SIZE
            
            if i == 0:
                # Head
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=GREEN, outline=WHITE, tags='snake')
            else:
                # Body
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=DARK_GREEN, outline=WHITE, tags='snake')
        
        # Draw food
        fx1 = self.food.position[0] * GRID_SIZE
        fy1 = self.food.position[1] * GRID_SIZE
        fx2 = fx1 + GRID_SIZE
        fy2 = fy1 + GRID_SIZE
        self.canvas.create_oval(fx1, fy1, fx2, fy2, fill=RED, outline=WHITE, tags='food')
    
    def run(self):
        """Start the game"""
        self.update()
        self.root.mainloop()
        
        # Cleanup: release MediaPipe task and camera
        if self.hand_landmarker is not None:
            try:
                self.hand_landmarker.close()
            except Exception:
                pass
            self.hand_landmarker = None
        if self.cap is not None:
            self.cap.release()
            self.cap = None
            cv2.destroyAllWindows()

if __name__ == '__main__':
    game = Game()
    game.run()

