import pygame, random, sys, psycopg2, json

pygame.init()


W,H = 600,400
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Змейка")


GREEN = (0, 200, 0)
RED =(200,0,0)
BLACK =(0,0, 0)
WHITE = (255,255, 255)
BLUE = (0, 0, 255)
YELLOW =(255, 255, 0)
ORANGE =(255,165, 0)

size =20
speed =8
font =pygame.font.SysFont("Arial",25)

def show_text(txt,color, pos):
    text = font.render(txt,True, color)
    screen.blit(text,pos)

def new_food(snake):
    while True:
        fx = random.randrange(0,W -size,size)
        fy = random.randrange(0,H -size,size)
        if [fx, fy] not in snake:
            return [fx,fy]

DB_CONFIG = {
    "dbname":"postgres",
    "user":"postgres",
    "password":"1234",
    "host":"localhost",
    "port":"5432"
}

def get_or_create_user():
    username =input("Введи имя: ").strip()
    conn =psycopg2.connect(**DB_CONFIG)
    cur =conn.cursor()
    cur.execute("SELECT id FROM users WHERE username=%s",(username,))
    user =cur.fetchone()
    if user:
        user_id =user[0]
        print(f"{username}! Загружаем Сохр")
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id =cur.fetchone()[0]
        conn.commit()
        print(f"Велком {username}!")
    cur.close()
    conn.close()
    return user_id

def save_game(user_id, score, level, snake, dx, dy, food, food_weight):
    conn =psycopg2.connect(**DB_CONFIG)
    cur =conn.cursor()
    snake_json =json.dumps(snake)
    food_json =json.dumps(food)
    cur.execute("""
        INSERT INTO user_score (user_id, score, level, snake, dx, dy, food, food_weight)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """, (user_id, score, level, snake_json, dx, dy, food_json, food_weight))
    conn.commit()
    cur.close()
    conn.close()
    print("Сохр")

def load_last_state(user_id):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("""
        SELECT score, level, snake, dx, dy, food, food_weight
        FROM user_score
        WHERE user_id=%s
        ORDER BY id DESC
        LIMIT 1
    """, (user_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row:
        score, level, snake_json, dx, dy, food_json, food_weight = row
        snake =json.loads(snake_json)
        food =json.loads(food_json)
        return score,level,snake,dx, dy,food,food_weight
    else:
        return 0, 1, [[100,100]], size, 0,[150,150], 1


def save_game2(user_id, score, level):
    conn =psycopg2.connect(**DB_CONFIG)
    cur =conn.cursor()
    snake_json =json.dumps(snake)
    food_json =json.dumps(food)
    cur.execute("""
        INSERT INTO user_score2 (user_id, score, level)
        VALUES (%s,%s,%s)
    """, (user_id, score, level))
    conn.commit()
    cur.close()
    conn.close()
    print("Сохр")

user_id = get_or_create_user()
score, level, snake, dx, dy, food, food_weight = load_last_state(user_id)

clock = pygame.time.Clock()
running = True
paused = False

food_spawn_time = pygame.time.get_ticks()
FOOD_LIFETIME = 3000


while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and dy == 0:
        dx, dy = 0, -size
    elif keys[pygame.K_DOWN] and dy == 0:
        dx, dy = 0, size
    elif keys[pygame.K_LEFT] and dx == 0:
        dx, dy = -size, 0
    elif keys[pygame.K_RIGHT] and dx == 0:
        dx, dy = size, 0
    elif keys[pygame.K_p]:
        paused = True
        save_game2(user_id, score, level)
        while paused:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            keys2 = pygame.key.get_pressed()
            if keys2[pygame.K_r]:
                paused = False
            show_text("Пауза --- Нажмите R для прод", RED, (W//2 - 180, H//2))
            pygame.display.flip()
            clock.tick(5)

    head = [snake[-1][0] + dx, snake[-1][1] + dy]
    snake.append(head)


    if head[0] < 0 or head[0] >= W or head[1] < 0 or head[1] >= H or head in snake[:-1]:
        running = False


    if head == food:
        score += food_weight
        food = new_food(snake)
        food_weight = random.choice([1, 2, 5])
        food_spawn_time = pygame.time.get_ticks()
        if score % 4 == 0:
            level += 1
            speed += 2
    else:
        del snake[0]

    if pygame.time.get_ticks() - food_spawn_time > FOOD_LIFETIME:
        food = new_food(snake)
        food_weight = random.choice([1, 2, 5])
        food_spawn_time = pygame.time.get_ticks()

    screen.fill(WHITE)

    if food_weight ==1:
        fcolor =RED
    elif food_weight==2:
        fcolor =ORANGE
    else:
        fcolor =YELLOW

    pygame.draw.rect(screen, fcolor, (*food,size,size))

    for s in snake:
        pygame.draw.rect(screen, GREEN, (*s,size,size))

    show_text(f"Score: {score}", BLUE, (10, 10))
    show_text(f"Level: {level}", BLUE, (W - 130, 10))
    show_text(f"Food: {food_weight}", BLUE, (W // 2 - 40, 10))

    pygame.display.flip()
    clock.tick(speed)

screen.fill(BLACK)
show_text("GAME OVER!", RED, (W//2 -100, H//2 -20))
show_text(f"Score:{score}   Level: {level}",WHITE, (W//2 -100, H//2 +20))
pygame.display.update()
pygame.time.wait(2000)
pygame.quit()
