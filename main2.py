# Pygame Template 1.0

# Import the pygame and system modules
import pygame
import sys

# --- Constants --- #
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60  # Frames per second
WHITE = (255, 255, 255)  # RGB triplet saved in a tuple
CYAN = (0,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)

# --- Initialize Pygame ---
pygame.init()

# --- Screen setup --- #
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Template")

# --- Clock setup --- #
clock = pygame.time.Clock()  # Note the capital C in the word Clock!

# --- Game loop --- #
running = True
while running:
    # --- Listen for and handle events --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Type the QUIT event in UPPERCASE!
            running = False

    # --- Game logic --- #
    # (This is where you'll put your game's logic)

    # --- Draw --- #
    screen.fill(WHITE)  # Fill screen background with white

    # (This is where you'll draw your game objects)
    def draw_rectangle(screen = screen, rect = [100,100,100,100], color = BLACK, thickness = 100):
        pygame.draw.rect(screen, color, rect, thickness)
    
    def draw_circle(screen = screen, center = [100,100], radius = 100, color = BLACK, thickness = 100):
        pygame.draw.circle(screen, color, center, radius, thickness)
    
    def draw_line(screen = screen, color = BLACK, point1 = (100, 100), point2 = (100, 100), thickness = 100):
        pygame.draw.line(screen, color, point1, point2, thickness)

    draw_rectangle(color = RED, rect = [400,400, 200, 100])
    draw_circle(color = (0,0,255), center = [300, 300])
    draw_line(point1 = [500,100], point2 = [700, 150], thickness = 20)
    
    pygame.display.flip()  # Update the display

    # --- Limit frames per second (FPS) --- #
    clock.tick(FPS)

# --- Quit Pygame and exit system module --- #
pygame.quit()
sys.exit()
