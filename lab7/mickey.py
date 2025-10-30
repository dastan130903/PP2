import pygame,math,datetime
pygame.init()

#miki mouse time 
bg=pygame.image.load('base_micky (1).jpg')
hand_min=pygame.image.load('minute.png')

hand_sec=pygame.image.load('second.png')

size=bg.get_size()
win=pygame.display.set_mode(size)

pygame.display.set_caption('Chasiki')

mid=(size[0]//2,size[1]//2)

fps=pygame.time.Clock()
runn=True

while runn:
    for e in pygame.event.get():
        if e.type==pygame.QUIT:runn=False
    now=datetime.datetime.now()
    
    mins=now.minute+now.second /60
    secs=now.second+now.microsecond /1_000_000

    ang_m=-6*mins-42  #6
    ang_s=-6*secs

    rot_m=pygame.transform.rotate(hand_min,ang_m)
    
    rot_s=pygame.transform.rotate(hand_sec ,ang_s)

    rect_m=rot_m.get_rect(center=mid)
    rect_s=rot_s.get_rect(center=mid)
#rg
    win.blit(bg,(0,0))
    win.blit(rot_m,rect_m)
    
    win.blit(rot_s,rect_s)

    fontik=pygame.font.SysFont('Comic Sans MS', 22)
    txt=fontik.render('Mickey chsd',True,(30,30, 30))
    win.blit(txt,(15, 15))

    pygame.display.flip()
    fps.tick(30)

pygame.quit()
