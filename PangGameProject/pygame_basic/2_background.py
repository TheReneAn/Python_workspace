import pygame

pygame.init()       # initializtion (Must do it)

# Set Window Size
screen_width = 480
screen_height = 640

screen = pygame.display.set_mode((screen_width, screen_height))

# Set Screen Title
pygame.display.set_caption("Pang Game_Rene's project")    # Game Name

# Background image
#background = pygame.image.load("C:\\Users\\auj08\\Desktop\\Python_workspace\\PangGameProject\\pygame_basic\\background.png")

# Event loof
running = True      # Is this game running now?
while running:
    for event in pygame.event.get():    # What kind of event has happened?
        if event.type == pygame.QUIT:   # Has an event happened to close the window?
            running = False             # The game was finished

    screen.fill((0, 0, 255))            # (Way 1) fill
    #screen.blit(background, (0,0))     # (Way 2) Use path... Make the background

    pygame.display.update()             # Make the game background again (Each frame)

# Exit Pygame 
pygame.quit()
