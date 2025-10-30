import pygame

pygame.init()
WIDTH, HEIGHT =800,600
screen =pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Red Ball by Dast")

WHITE =(255,255, 255)
RED =(255, 30,30)

BG_COLOR =(230,230,255)   # голубоваn


RADIUS =25
x, y = WIDTH //2,HEIGHT//2
STEP =20

clock = pygame.time.Clock()
running =True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and y - RADIUS - STEP>=0:
        y -= STEP
    elif keys[pygame.K_DOWN] and y +RADIUS +STEP <= HEIGHT:
        y += STEP
    elif keys[pygame.K_LEFT] and x -RADIUS -STEP >= 0:
        x -= STEP
    elif keys[pygame.K_RIGHT] and x +RADIUS +STEP <=WIDTH:
        x += STEP


    screen.fill(BG_COLOR)
    pygame.draw.circle(screen,RED,(x,y) ,RADIUS)

    font = pygame.font.SysFont('Arial', 20)
    text = font.render('Red Ball by Dastan',True,(60,60,60))
    
    screen.blit(text,(10,10))
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
