import pygame


pygame.init()

#screen size
screen_width = 600
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))

circle_radius = 25
circle_x = (screen_width - circle_radius) // 2
circle_y = (screen_height - circle_radius) // 2

white = (255, 255, 255)
red = (255, 0, 0)

def draw_circle(x, y):
    pygame.draw.circle(screen, red, (x, y), circle_radius)
    
# main game loop
running = True
while running:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                circle_y -= 20
            elif event.key == pygame.K_DOWN:
                circle_y += 20
            elif event.key == pygame.K_LEFT:
                circle_x -= 20
            elif event.key == pygame.K_RIGHT:
                circle_x += 20
    # keep the ball within the screen bounds
    circle_x = max(circle_x, circle_radius)
    circle_y = max(circle_y, circle_radius)
    circle_x = min(circle_x, screen_width - circle_radius)
    circle_y = min(circle_y, screen_height - circle_radius)
    # clear the screen
    screen.fill(white)

    # draw the circle
    draw_circle(circle_x, circle_y)
    # update the screen
    pygame.display.update()
# quit Pygame
pygame.quit()
