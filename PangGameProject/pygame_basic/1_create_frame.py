import pygame

pygame.init()       # initializtion (Must do it)

# Set Window Size
screen_width = 480
screen_height = 640

screen = pygame.display.set_mode((screen_width, screen_height))

# Set Screen Title
pygame.display.set_caption("Pang Game_Rene's project")    # Game Name

# Event loof
running = True      # Is this game running now?
while running:
    for event in pygame.event.get():    # What kind of event has happened?
        if event.type == pygame.QUIT:   # Has an event happened to close the window?
            running = False

# Exit Pygame 
pygame.quit()
