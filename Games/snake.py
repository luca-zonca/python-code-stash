"""Step 1: Import required libraries"""
import pygame
import time
import random

"""Step 2: Initialize pygame and set up display"""
# Initialize all the pygame modules
pygame.init()

# Define colors using RGB values
white = (255,255,255)
black = (0,0,0)
red = (213,50,80)
green = (0,255,0)
blue = (50,153,213)

# Set the dimensions of the game window
dis_width = 600
dis_height = 400

# Set up the display
dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption("Snake")

# Helps managing how fast the game updates
clock = pygame.time.Clock()

# Size of each segment of the snake
snake_block = 10

# Controls how fast the snake moves
snake_speeds = {"Easy":10, "Medium":15, "Hard":25}

"""Step 3: Create functions to draw the snake and display messages"""
# Takes the size of the snake block and a list of snake positions. It draws each block of the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# Display the difficulty menu
def choose_difficulty():
    difficulty = None
    while difficulty not in snake_speeds:
        dis.fill(blue)
        message("Choose difficulty: E-Easy, M-Medium, H-Hard", white)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    difficulty = "Easy"
                elif event.key == pygame.K_m:
                    difficulty = "Medium"
                elif event.key == pygame.K_h:
                    difficulty = "Hard"

    return snake_speeds[difficulty]

# Renders text on the screen
def message(msg, color):
    font_style = pygame.font.SysFont(None, 30)
    mesg = font_style.render(msg, True, color)
    mesg_rect = mesg.get_rect(center=(dis_width/2, dis_height/2))
    dis.blit(mesg, mesg_rect.topleft)

"""Step 4: Set up the game loop"""
def gameloop():
    # Get the chosen snake speed
    snake_speed = choose_difficulty()

    # Game state managers
    game_over = False
    game_close = False

    # Snake starting position
    x1 = dis_width/2
    y1 = dis_height/2

    # Snake movement managers
    x1_change = 0
    y1_change = 0
    
    # Keeps track of the snake's body segments
    snake_List = []
    Length_of_snake = 1

    # Food's coordinates
    foodx = round(random.randrange(0, dis_width - snake_block)/10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block)/10.0) * 10.0

    while not game_over:
        
        # When the game ends, display a message and give options to quit or restart
        while game_close == True:
            dis.fill(blue)
            message("You lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameloop()
        
        for event in pygame.event.get():
            # Exits the game if the window is closed
            if event.type == pygame.QUIT:
                game_over = True
            # Handles keyboard inputs to change the direction of the snake
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Updates the snake's position based on the direction change
        x1 += x1_change
        y1 += y1_change

        # Create a new snake head segment
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        # Add the new head to the snake's body
        snake_List.append(snake_head)
        # Remove the tail segment if the snake is too long (illusion of moving forward, tail segment removed when new head added)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # If the snake eats the food, it grows longer and new food is placed randomly
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        # Checking wall collision: if the snake's head (x1,y1) moves outside the boundaries of the screen, game over is triggered
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        
        # Checking self collision: if the snake's head collides with any part of its body, game over is triggered
        for segment in snake_List[:-1]:
            if segment[0] == x1 and segment[1] == y1:
                game_close = True

        # Rendering: clear the screen and redraws the snake and the food
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        our_snake(snake_block, snake_List)

        # Rendering: updates the entire display surface to show the latest changes
        pygame.display.update()
        
        # Controls the game's frame rate, affecting how fast the snake moves
        clock.tick(snake_speed)
    
    # Stop pygame and exit the program, when the game ends
    pygame.quit()
    quit()

gameloop()