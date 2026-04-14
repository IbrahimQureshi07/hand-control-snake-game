import pygame
import random
import sys

# ============================================
# CONTROL MODE SETTING - YAHAN CHANGE KARO
# ============================================
# Line 8 par CONTROL_MODE change karo:
# 'keyboard' = Arrow keys se khelo (abhi ke liye)
# 'hand' = Hand gestures se khelo (baad mein camera ke saath)
CONTROL_MODE = 'keyboard'  # YAHAN 'keyboard' ya 'hand' likho

# ============================================
# GAME SETTINGS
# ============================================
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
DARK_GREEN = (0, 200, 0)
BLUE = (0, 0, 255)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self):
        self.length = 3
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = RIGHT
        self.color = GREEN
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
    
    def render(self, surface):
        for i, p in enumerate(self.positions):
            r = pygame.Rect((p[0] * GRID_SIZE, p[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
            if i == 0:
                pygame.draw.rect(surface, self.color, r)
                pygame.draw.rect(surface, WHITE, r, 1)
            else:
                pygame.draw.rect(surface, DARK_GREEN, r)
                pygame.draw.rect(surface, WHITE, r, 1)

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()
    
    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    
    def render(self, surface):
        r = pygame.Rect((self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, WHITE, r, 1)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Snake Game - Arrow Keys to Play')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        self.snake = Snake()
        self.food = Food()
        self.game_over = False
        
        # For hand control (will be used later)
        self.cap = None
        if CONTROL_MODE == 'hand':
            self.init_hand_control()
    
    def init_hand_control(self):
        """Initialize hand control - will be implemented when camera works"""
        # TODO: Add MediaPipe hand detection here
        # import cv2
        # import mediapipe as mp
        # self.cap = cv2.VideoCapture(0)
        # self.mp_hands = mp.solutions.hands
        # self.hands = self.mp_hands.Hands()
        pass
    
    def get_hand_direction(self):
        """Get direction from hand gesture - will be implemented later"""
        # TODO: Implement hand gesture detection
        # This will return UP, DOWN, LEFT, or RIGHT based on hand position
        return None
    
    def handle_keyboard_input(self):
        """Handle arrow key input"""
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP] and self.snake.direction != DOWN:
            self.snake.direction = UP
        elif keys[pygame.K_DOWN] and self.snake.direction != UP:
            self.snake.direction = DOWN
        elif keys[pygame.K_LEFT] and self.snake.direction != RIGHT:
            self.snake.direction = LEFT
        elif keys[pygame.K_RIGHT] and self.snake.direction != LEFT:
            self.snake.direction = RIGHT
    
    def handle_hand_input(self):
        """Handle hand gesture input - will be implemented later"""
        if CONTROL_MODE == 'hand':
            direction = self.get_hand_direction()
            if direction:
                # Prevent reversing into itself
                if (direction == UP and self.snake.direction != DOWN) or \
                   (direction == DOWN and self.snake.direction != UP) or \
                   (direction == LEFT and self.snake.direction != RIGHT) or \
                   (direction == RIGHT and self.snake.direction != LEFT):
                    self.snake.direction = direction
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r and self.game_over:
                        # Restart game
                        self.snake.reset()
                        self.food.randomize_position()
                        self.game_over = False
            
            if not self.game_over:
                # Handle input based on control mode
                if CONTROL_MODE == 'keyboard':
                    self.handle_keyboard_input()
                elif CONTROL_MODE == 'hand':
                    self.handle_hand_input()
                
                # Update snake
                if not self.snake.update():
                    self.game_over = True
                
                # Check if snake ate food
                if self.snake.get_head_position() == self.food.position:
                    self.snake.length += 1
                    self.snake.score += 10
                    self.food.randomize_position()
                    # Make sure food doesn't spawn on snake
                    while self.food.position in self.snake.positions:
                        self.food.randomize_position()
            
            # Render
            self.screen.fill(BLACK)
            self.snake.render(self.screen)
            self.food.render(self.screen)
            
            # Display score
            score_text = self.font.render(f'Score: {self.snake.score}', True, WHITE)
            self.screen.blit(score_text, (10, 10))
            
            # Display control mode
            mode_text = self.small_font.render(f'Mode: {CONTROL_MODE.upper()}', True, WHITE)
            self.screen.blit(mode_text, (10, 50))
            
            # Game over screen
            if self.game_over:
                game_over_text = self.font.render('GAME OVER!', True, RED)
                restart_text = self.small_font.render('Press R to Restart', True, WHITE)
                text_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 20))
                restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20))
                self.screen.blit(game_over_text, text_rect)
                self.screen.blit(restart_text, restart_rect)
            
            pygame.display.update()
            self.clock.tick(10)  # Game speed

if __name__ == '__main__':
    game = Game()
    game.run()




