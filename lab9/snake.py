import pygame, random, sys

pygame.init()

# размеры окна----
W,H = 600,400
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("Змейка")

# цвета--
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# настройки змейки==
size =20  # блок сайз
speed =8  # спид гейм

font = pygame.font.SysFont("Arial",25)

def show_text(txt,color,pos):
    text = font.render(txt,True,color)
    screen.blit(text,pos)

def new_food(snake):
    while True:
        fx = random.randrange(0,W -size,size)
        fy = random.randrange(0,H -size, size)
        if [fx, fy] not in snake:
            return [fx,fy]

snake = [[100, 100]]
dx, dy = size,0
food= new_food(snake)
score =0
level =1

clock =pygame.time.Clock()
running =True

###
food_weight = 1                   # вес текущей еды
food_spawn_time = pygame.time.get_ticks()
FOOD_LIFETIME = 3000              # время жизни



while running:
    for e in pygame.event.get():
        if e.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and dy==0:
        dx, dy =0,-size
    elif keys[pygame.K_DOWN] and dy==0:
        dx, dy =0,size
    elif keys[pygame.K_LEFT] and dx ==0:
        dx,dy =-size,0
    elif keys[pygame.K_RIGHT] and dx ==0:
        dx, dy =size,0

    # движение кобры
    head =[snake[-1][0]+dx,snake[-1][1]+dy]
    snake.append(head)
    # стенка чек
    if head[0] <0 or head[0] >=W or head[1]<0 or head[1]>=H:
        running =False
    # в себя
    if head in snake[:-1]:
        running =False

    # +food
    if head ==food:


        score+=food_weight
        food =new_food(snake)

        food_weight = random.choice([1, 2, 5])
        food_spawn_time = pygame.time.get_ticks()

        if score % 4==0:
            level +=1
            speed+=2
    else:
        del snake[0]


    if pygame.time.get_ticks() -food_spawn_time >FOOD_LIFETIME:
        food = new_food(snake)
        food_weight = random.choice([1, 2, 5])
        food_spawn_time = pygame.time.get_ticks()

    screen.fill(WHITE)

    if food_weight== 1:
        fcolor = RED
    elif food_weight==2:
        fcolor = ORANGE
    else:
        fcolor =YELLOW

    pygame.draw.rect(screen, fcolor,(*food,size,size))  #фуд

    for s in snake:
        pygame.draw.rect(screen,GREEN,(*s,size,size))  #анаконда
    show_text(f"Score: {score}",BLUE, (10,10))
    show_text(f"Level: {level}",BLUE, (W - 130,10))
    show_text(f"Food: {food_weight}", BLUE,(W//2- 40,10))

    pygame.display.flip()
    clock.tick(speed)

screen.fill(BLACK)
show_text("GAME OVER!",RED,(W//2 -100,H//2 -20))
show_text(f"Score:{score}   Level: {level}",WHITE, (W//2 -100,H//2 +20))
pygame.display.update()
pygame.time.wait(2000)
pygame.quit()
