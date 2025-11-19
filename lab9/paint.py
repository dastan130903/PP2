import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []

    tool = 'pen'
    start_pos = None
    drawing = False
    color = (0, 0, 255)

    #
    canvas = pygame.Surface((640, 480))
    canvas.fill((0, 0, 0))

    while True:

        pressed = pygame.key.get_pressed()

        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return


                if event.key ==pygame.K_r:
                    mode ='red'
                    color =(255,0,0)
                elif event.key ==pygame.K_g:
                    mode ='green'
                    color = (0,255,0)
                elif event.key == pygame.K_b:
                    mode = 'blue'
                    color =(0,0,255)

                # инструменты
                elif event.key ==pygame.K_p:
                    tool ='pen' #ряука P
                elif event.key ==pygame.K_c:
                    tool ='circle' # треугольник C
                elif event.key ==pygame.K_l:
                    tool ='rect' # прямоугольник L
                
                elif event.key ==pygame.K_e:
                    tool ='eraser' # sterka
                elif event.key== pygame.K_q:
                    tool ='square'
                    
                elif event.key ==pygame.K_t:
                    tool ='rect_triangle'
                elif event.key ==pygame.K_y:
                    tool ='equ_triangle'
                elif event.key==pygame.K_d:
                    tool='rhombus'
                elif event.key == pygame.K_SPACE:
                    canvas.fill((0, 0, 0))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
                    start_pos = event.pos
                elif event.button == 3:
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEBUTTONUP:
                if drawing:
                    end_pos = event.pos
                    x1,y1 = start_pos
                    x2,y2 =end_pos

                    if tool =='rect' and start_pos:
                        rect = pygame.Rect(min(x1,x2), min(y1,y2),
                                           abs(x1 -x2), abs(y1- y2))
                        pygame.draw.rect(canvas,color, rect, 2)
                    elif tool =='circle' and start_pos:

                        radius_circle = int(((x2 -x1) **2 + (y2 -y1) **2) **0.5)
                        pygame.draw.circle(canvas,color,start_pos, radius_circle, 2)
                    elif tool == 'square':
                        side = max(abs(x2 -x1), abs(y2- y1))
                        rect = pygame.Rect(x1,y1, side,side)
                        pygame.draw.rect(canvas,color, rect, 2)
                    elif tool =='rect_triangle':
                        points = [(x1,y1), (x1,y2),(x2, y2)]
                        pygame.draw.polygon(canvas,color, points, 2)
                    elif tool =='equ_triangle':
                        width = x2 -x1
                        height = (3 ** 0.5/2) *abs(width)
                        if y2 <y1:
                            height = -height
                        points = [(x1,y1), (x1 +width, y1), (x1 +width /2,y1 - height)]
                        pygame.draw.polygon(canvas,color,points, 2)
                    elif tool =='rhombus':
                        mx = (x1 +x2)/2
                        my = (y1 +y2) /2
                        points = [(mx,y1),(x2,my),(mx,y2),(x1,my)]
                        pygame.draw.polygon(canvas, color, points, 2)

                drawing = False

            if event.type == pygame.MOUSEMOTION and drawing:
                position = event.pos
                if tool == 'pen':
                    pygame.draw.circle(canvas, color, position, radius)
                elif tool == 'eraser':
                    pygame.draw.circle(canvas, (0, 0, 0), position, radius)

        #
        screen.blit(canvas, (0, 0))

        pygame.display.flip()
        clock.tick(60)


def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode =='blue':
        color = (c1, c1,c2)
    elif color_mode== 'red':
        color = (c2,c1, c1)
    elif color_mode =='green':
        color = (c1,c2,c1)

    dx = start[0]-end[0]
    dy = start[1]-end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()
