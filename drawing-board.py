import pygame
import sys

pygame.init()

width, height = 1000, 600
screen = pygame.display.set_mode((width, height))
screen.fill((255, 255, 255))  # background color

#storing mouse positions
old_mouse_pos = None

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SKIN = (255, 224, 189)  # skin 
BROWN = (102, 51, 0)    # hair 
BLUE = (0, 0, 255)      # dress 
PINK = (255, 182, 193)  # cccessory 
GRAY = (128, 128, 128)  # glasses and shoes

# character size
pixel_size = 5  

# art critic
girl_design = [
    [0, 0, 3, 3, 3, 3, 3, 3, 0, 0],
    [0, 3, 2, 2, 2, 2, 2, 2, 3, 0],
    [3, 2, 6, 5, 5, 5, 5, 6, 2, 3],
    [3, 2, 5, 2, 2, 2, 2, 5, 2, 3],
    [3, 2, 2, 2, 2, 2, 2, 2, 2, 3],
    [3, 4, 4, 4, 1, 1, 4, 4, 4, 3],
    [0, 4, 4, 1, 1, 1, 1, 4, 4, 0],
    [0, 4, 4, 1, 1, 1, 1, 4, 4, 0],
    [0, 0, 4, 4, 4, 4, 4, 4, 0, 0],
    [0, 0, 6, 6, 0, 0, 6, 6, 0, 0],  # Shoes
]

# function to draw the pixelated character
def draw_character(x, y, design, colors):
    for row in range(len(design)):
        for col in range(len(design[row])):
            color_index = design[row][col]
            if color_index != 0:
                color = colors[color_index]
                pygame.draw.rect(screen, color, (x + col * pixel_size, y + row * pixel_size, pixel_size, pixel_size))


# define the position and size of the canvas to save
canvas_x = 0  # x-coordinate of the top-left corner of the canvas
canvas_y = 0  # y-coordinate of the top-left corner of the canvas
canvas_width = 800  
canvas_height = 500 

# create a rect object for the canvas
canvas_rect = pygame.Rect(canvas_x, canvas_y, canvas_width, canvas_height)

# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # get current mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Draw line when mouse is pressed
    if pygame.mouse.get_pressed()[0]:  # if left mouse button is pressed
        if old_mouse_pos is not None:  # if we have a previous position to draw from
            pygame.draw.line(screen, (0,0,0), old_mouse_pos, mouse_pos)
        old_mouse_pos = mouse_pos
    else:
        old_mouse_pos = None

    draw_character(800, 500, girl_design, [WHITE, BLACK, SKIN, BROWN, BLUE, PINK, GRAY])

    #drawing out rectangle of canvas area as a test vvv
    #pygame.draw.rect(screen, (50,255,255),canvas_rect)

    canvas_surface = screen.subsurface(canvas_rect).copy()
    pygame.image.save(canvas_surface, "drawing.png")

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()