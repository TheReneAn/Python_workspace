import pygame

pygame.init()       # initializtion (Must do it)

# Set Window Size
#screen_width = 480
screen_width = 900
screen_height = 550

screen = pygame.display.set_mode((screen_width, screen_height))

# Set Screen Title
pygame.display.set_caption("Pang Game_Rene's project")    # Game Name

# FPS
clock = pygame.time.Clock()

# Background image
background = pygame.image.load("C:\\Users\\auj08\\Desktop\\Python_workspace\\PangGameProject\\pygame_basic\\background.jpg")

# Character (Sprite)
character = pygame.image.load("C:\\Users\\auj08\\Desktop\\Python_workspace\\PangGameProject\\pygame_basic\\character.png")

character_size = character.get_rect().size          # Get character size
character_width = character_size[0]                 # Size of the character width size
character_height = character_size[1]

character_x_pos = (screen_width / 2) - (character_width / 2)    # Set the character's Location at half of the width size in the screen
character_y_pos = screen_height - character_height  # At the end of the screen

# Move Coordinate
to_x = 0
to_y = 0

# Move Speed
character_speed = 0.6

# Enemy character
enemy = pygame.image.load("C:\\Users\\auj08\\Desktop\\Python_workspace\\PangGameProject\\pygame_basic\\enemy.png")

enemy_size = enemy.get_rect().size          # Get character size
enemy_width = enemy_size[0]                 # Size of the character width size
enemy_height = enemy_size[1]

enemy_x_pos = (screen_width / 2) - (enemy_width / 2)    # Set the character's Location at half of the width size in the screen
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)  # At the end of the screen

# Event loof
running = True      # Is this game running now?
while running:
    dt = clock.tick(60)                 # Set Frame number per second on the game screen

    for event in pygame.event.get():    # What kind of event has happened?
        if event.type == pygame.QUIT:   # Has an event happened to close the window?
            running = False             # The game was finished
        
        if event.type == pygame.KEYDOWN:    # Check puch the key? or not
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:      # If the key up, stop the action
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # Character screeen boundary
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height    

    # Set Collition system
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # Chect Collition
    if character_rect.colliderect(enemy_rect):
        print("It crashed")
        running = False

    # Make image on the screen
    screen.blit(background, (0,0))      # Make the background
    screen.blit(character, (character_x_pos, character_y_pos))  # Make the Character on the screen
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    pygame.display.update()             # Make the game background again (Each frame)

# Exit Pygame 
pygame.quit()
