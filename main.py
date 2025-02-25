import pygame
import sys
import colors
import config  # Import the config module

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))  # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def main():

    screen = init_game()
    clock = pygame.time.Clock() # Initialize the clock object
    
    running = True
    while running:
        running = handle_events()
        screen.fill(colors.WHITE)  # Use color from config
        
        # Draw the initials on the screen
        def draw_polygon(points, screen = screen, color = colors.ARTIFICIAL_BANANA_YELLOW,  thickness=0):
            pygame.draw.polygon(screen, color, points, thickness)
        
        points1 = [
            (300, 200),  
            (400, 350),  
            (100, 400),  
            (0, 400),  
            (500, 500)   
        ]

        #outline1
        points2 = [
            (300, 200),  
            (400, 350),  
            (100, 400),  
            (0, 400),  
            (500, 500)   
        ]

        points3 = [
            (750, 50),  
            (750, 550),  
            (550, 550),  
            (700, 50),  
            (750, 50)   
        ]
        
        #outline2
        points4 = [
            (750, 50),  
            (750, 550),  
            (550, 550),  
            (700, 50),  
            (750, 50)   
        ]

        #outline3
        points5 = [
            (400, 0),  
            (420, 0),  
            (430, 10),  
            (420, 20),  
            (390, 10)   
        ]
        
        draw_polygon(points = points1,)
        draw_polygon(color = colors.BLACK, points = points2, thickness=10)

        draw_polygon(color = colors.WINDOWS_XP_GRASS_GREEN, points = points3,)
        draw_polygon(color = colors.YOUTUBE_AD_RED, points = points4, thickness=2)

        draw_polygon(color = colors.WEIRDLY_SATURATED_SKY_BLUE, points = points5, thickness=5)
        
        pygame.display.flip()

        # Limit frame rate to certain number of frames per second (FPS)
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
