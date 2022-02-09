import pygame, sys

pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('DVD')

square = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 60,60)

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

square_speed_x = 7
square_speed_y = 7

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    square.x += square_speed_x
    square.y += square_speed_y

    if square.top <= 0 or square.bottom >= screen_height:
        square_speed_y *= -1
    if square.left <=0 or square.right >= screen_width:
        square_speed_x *= -1

    screen.fill(bg_color)
    pygame.draw.rect(screen,light_grey,square)

    pygame.display.flip()
    clock.tick(60)