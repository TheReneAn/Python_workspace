import os
import pygame

########################################################################################################
#                                   Basic initialization (Must do it)                                  #
########################################################################################################

pygame.init()       # initialization (Must do it)

# Set Window Size
screen_width = 900
screen_height = 550

screen = pygame.display.set_mode((screen_width, screen_height))

# Set Screen Title
pygame.display.set_caption("Pang Game_Rene's project")  # Game Name

# FPS
clock = pygame.time.Clock()

########################################################################################################
#           User game initialization (Background, Game image, Coordinate, Speed, Font etc)             #
########################################################################################################

current_path = os.path.dirname(__file__)                # Returns the location of the current file
image_path = os.path.join(current_path, "images")       # Returns the location of the images folder

########################################### Background image ########################################### 
background = pygame.image.load(os.path.join(image_path, "background.jpg"))

################################################ Stage #################################################
stage = pygame.image.load(os.path.join(image_path, "stage.png"))

stage_size = stage.get_rect().size          # Get stage size
stage_height = stage_size[1]

########################################### Character (Sprite) ##########################################
character = pygame.image.load(os.path.join(image_path, "character.png"))

character_size = character.get_rect().size          # Get character size
character_width = character_size[0]                 # Size of the character width size
character_height = character_size[1]

# Set the character's Location at half of the width size in the screen
character_x_pos = (screen_width / 2) - (character_width / 2) 
character_y_pos = screen_height - character_height - stage_height  # At the end of the screen

# Move Coordinate
character_to_x = 0

# Move Speed
character_speed = 5

################################################ Weapon ################################################
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))

weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# Weapon can shoot multiple times
weapons = []

weapon_speed = 10

################################################# Ball #################################################
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))
]

ball_speed_y = [-18, -15, -12, -9] 

balls = []

# First ball append
balls.append({
    "pos_x" : 50,       # x coordinate of a ball
    "pos_y" : 50,
    "img_idx" : 0,      # index of a ball
    "to_x" : 3,         # direction of x-axis movement
    "to_y" : -6,        # if the number is -3, it will move to left.
    "init_spd_y" : ball_speed_y[0]      # Fist speed
})

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

        if event.type == pygame.KEYDOWN:    # Check puch the key? or not
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

########################################################################################################
#                                       Character Position / boundary                                 #
########################################################################################################  

    character_x_pos += character_to_x

    # Character screeen boundary
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    ############################################## Weapon ##############################################
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons]

    # Remove weapons
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]

    ##################################### Definition Ball location #####################################
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # The effect of bouncing off a width wall
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1

        # The effect of bouncing off a height wall
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]    
        else:
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]

########################################################################################################
#                                       Collition initialization                                       #
########################################################################################################


########################################################################################################
#                                               Show to screen                                         #
########################################################################################################

    screen.blit(background, (0,0))      # Make the background

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    screen.blit(stage, (0, screen_height - stage_height))  # Make the Character on the screen
    screen.blit(character, (character_x_pos, character_y_pos))  # Make the Character on the screen

########################################################################################################
#                                       Basic Statements (Must do it)                                  #
########################################################################################################

    pygame.display.update()             # Make the game background again (Each frame)

# Exit Pygame 
pygame.quit()


