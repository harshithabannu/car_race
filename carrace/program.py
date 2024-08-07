import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 800
HEIGHT = 600
SPEED = 5

# Set up some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 128, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load the car images
player_car_image = pygame.image.load('car.png')
player_car_image = pygame.transform.scale(player_car_image, (100, 100))

computer_car_image = pygame.image.load('comp.png')
computer_car_image = pygame.transform.scale(computer_car_image, (100, 100))

# Set up the player car
player_car = player_car_image.get_rect(center=(WIDTH / 2, HEIGHT - 100))

# Set up the computer car
computer_car = computer_car_image.get_rect(center=(WIDTH / 2, 0))

# Set up the road
road = pygame.Rect(WIDTH / 2 - 200, 0, 400, HEIGHT)

# Set up the road lines
road_line_width = 10
road_line_color = WHITE
road_line_distance = 50

# Game loop
game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get a list of all keys currently being pressed down
    keys = pygame.key.get_pressed()

    # Move the player car
    if keys[pygame.K_LEFT] and player_car.x > road.x:
        player_car.x -= SPEED
    if keys[pygame.K_RIGHT] and player_car.x < road.x + road.width - 100:
        player_car.x += SPEED
    if keys[pygame.K_UP] and player_car.y > 0:
        player_car.y -= SPEED
    if keys[pygame.K_DOWN] and player_car.y < HEIGHT - 100:
        player_car.y += SPEED

    # Move the computer car
    computer_car.y += SPEED
    if computer_car.y > HEIGHT:
        computer_car.y = 0
        computer_car.x = random.randint(road.x, road.x + road.width - 100)

    # Fill the screen with green
    screen.fill(GREEN)

    # Draw the road
    pygame.draw.rect(screen, GRAY, road)

    # Draw the road lines
    for y in range(0, HEIGHT, road_line_distance):
        pygame.draw.rect(screen, road_line_color, (road.x + road.width / 2 - road_line_width / 2, y, road_line_width, road_line_distance))

    # Draw the player car
    screen.blit(player_car_image, player_car)

    # Draw the computer car
    screen.blit(computer_car_image, computer_car)

    # Check for collision
    if player_car.colliderect(computer_car):
        game_over = True

    if game_over:
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over!", 1, RED)
        screen.blit(text, (WIDTH / 2 - 75, HEIGHT / 2))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.delay(1000 // 60)
