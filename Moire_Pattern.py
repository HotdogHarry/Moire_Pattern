import pygame
from sys import exit

# Constants
WIDTH = 800
HEIGHT = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
fontSize = 60
rectangleWidth = 10
rectangleHeight = 600
offSet = 13
numRectangles = 20
angle = 5  # degrees

# Calculate the initial rectangleX value to center the rectangles
totalWidth = numRectangles * rectangleWidth + (numRectangles - 1) * offSet
rectangleX = (WIDTH - totalWidth) // 2
rectangleY = (HEIGHT - rectangleHeight) // 2  # Also center vertically

# Initialize Pygame
pygame.init()

# Set up Screen Display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moire Pattern")

running = True
while running:
    
    for event in pygame.event.get():
        
        # Check if user quits, if, so, quit code
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Draw Screen Display Background
    screen.fill(WHITE)

    # Multiple rectangles to draw for-loop
    for i in range(numRectangles):
        
        rect_x = rectangleX + i * (rectangleWidth + offSet)
        rectangle_1_Surface = pygame.Rect(rect_x, rectangleY, rectangleWidth, rectangleHeight)
        pygame.draw.rect(screen, BLACK, rectangle_1_Surface)

    # Create a surface for the rotated rectangles
    rotated_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    for i in range(numRectangles):
        
        rect_x = rectangleX + i * (rectangleWidth + offSet)
        rectangle_2_Surface = pygame.Rect(rect_x, rectangleY, rectangleWidth, rectangleHeight)
        pygame.draw.rect(rotated_surface, BLACK, rectangle_2_Surface)

    # Rotate the surface
    rotated_surface = pygame.transform.rotate(rotated_surface, angle)

    # Calculate the position to draw the rotated surface
    rect = rotated_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    # Draw the rotated surface
    screen.blit(rotated_surface, rect)

    # Update the Screen Display
    pygame.display.update()