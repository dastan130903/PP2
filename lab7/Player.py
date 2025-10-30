import pygame
import os

pygame.init();pygame.mixer.init()
W,H=700,200
win=pygame.display.set_mode((W,H))
pygame.display.set_caption("DasMP3")
fontik=pygame.font.SysFont('Comic Sans MS',26)

my_folder='music'
tracks=[os.path.join(my_folder,f)for f in os.listdir(my_folder)if f.endswith(('.mp3'))]

if not tracks:
    print('no musicsss')
    pygame.quit();exit()
now_song=0

def spin_disk():
    pygame.mixer.music.load(tracks[now_song])
    pygame.mixer.music.play()
    print(f"Song namee: {os.path.basename(tracks[now_song])}")
def stop_disk():
    pygame.mixer.music.stop();print('Stop')
def next_disk():
    global now_song
    now_song=(now_song+1)%len(tracks)
    spin_disk()
def prev_disk():
    global now_song
    now_song=(now_song-1)%len(tracks)
    spin_disk()
spin_disk()
run=True
clocky=pygame.time.Clock()

while run:
    win.fill((25,25,25))

    title=f"Now vibing: {os.path.basename(tracks[now_song])}"
    textik=fontik.render(title,True,(255,255,255))
    win.blit(textik,(25,80))

    pygame.display.flip()
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT:
            run=False
        elif ev.type==pygame.KEYDOWN:
            if ev.key==pygame.K_p:spin_disk()
            elif ev.key==pygame.K_s:stop_disk()
            elif ev.key==pygame.K_n:next_disk()
            elif ev.key==pygame.K_b:prev_disk()

    clocky.tick(30)

pygame.quit()
