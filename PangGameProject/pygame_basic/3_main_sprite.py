import pygame

pygame.init()       # initializtion (Must do it)

# Set Window Size
#screen_width = 480
screen_width = 900
screen_height = 550

screen = pygame.display.set_mode((screen_width, screen_height))

# Set Screen Title
pygame.display.set_caption("Pang Game_Rene's project")    # Game Name

# Background image
background = pygame.image.load("C:\\Users\\auj08\\Desktop\\Python_workspace\\PangGameProject\\pygame_basic\\background.jpg")

# Character (Sprite)
character = pygame.image.load("C:\\Users\\auj08\\Desktop\\Python_workspace\\PangGameProject\\pygame_basic\\character.png")

character_size = character.get_rect().size          # Get character size
character_width = character_size[0]                 # Size of the character width size
character_height = character_size[1]

character_x_pos = (screen_width / 2) - (character_width / 2)    # Set the character's Location at half of the width size in the screen
character_y_pos = screen_height - character_height  # At the end of the screen

# Event loof
running = True      # Is this game running now?
while running:
    for event in pygame.event.get():    # What kind of event has happened?
        if event.type == pygame.QUIT:   # Has an event happened to close the window?
            running = False             # The game was finished

    screen.blit(background, (0,0))      # Make the background

    screen.blit(character, (character_x_pos, character_y_pos))  # Make the Character on the screen

    pygame.display.update()             # Make the game background again (Each frame)

# Exit Pygame 
pygame.quit()
