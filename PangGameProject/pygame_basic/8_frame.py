import pygame

########################################################################################################
#                                   Basic initialization (Must do it)                                  #
########################################################################################################

pygame.init()       # initialization (Must do it)

# Set Window Size
#screen_width = 480
screen_width = 900
screen_height = 550

screen = pygame.display.set_mode((screen_width, screen_height))

# Set Screen Title
pygame.display.set_caption("Pang Game_Rene's project")    # Game Name

# FPS
clock = pygame.time.Clock()

########################################################################################################
#           User game initialization (Background, Game image, Coordinate, Speed, Font etc)             #
########################################################################################################



 
########################################################################################################
#                                       Event (Keybord, mouse etc)                                     #
########################################################################################################

# Event loof
running = True      # Is this game running now?
while running:
    dt = clock.tick(60)                 

    for event in pygame.event.get():    # What kind of event has happened?
        if event.type == pygame.QUIT:   # Has an event happened to close the window?
            running = False             # The game was finished

########################################################################################################
#                                       Character Position / boundary                                 #
########################################################################################################  



########################################################################################################
#                                       Collition initialization                                       #
########################################################################################################

    # Chect Collition
    if character_rect.colliderect(enemy_rect):
        print("It crashed")
        running = False

########################################################################################################
#                                               Show to screen                                         #
########################################################################################################



########################################################################################################
#                                       Basic Statements (Must do it)                                  #
########################################################################################################

    pygame.display.update()             # Make the game background again (Each frame)

# Exit Pygame 
pygame.quit()
