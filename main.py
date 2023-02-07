import sys
import pygame
from spike import Spike
from player import Player

pygame.init()
pygame.key.set_repeat(150, 150)

FPS = 60
RESO = (800,800)
screen = pygame.display.set_mode(RESO)

font = pygame.font.SysFont("Segoe UI", 50)

def calcule_score(score, toucher):
    if type(toucher) == bool:
        if toucher == False:
            score += 1
        elif toucher == True:
            player.update(0, RESO)
            player.affichage(screen)
            print(score)
            pygame.time.wait(1000)
            pygame.quit()
            sys.exit()
    return score

score = 0

spike = Spike(RESO[1], lenth_lvl=4, spike_max=8, spike_total=10, adding_lvl=0.5)
player = Player(spike)

spike.update()

spike.affichage(screen, RESO)
player.affichage(screen)
pygame.display.flip()
pygame.time.wait(1000)
clock = pygame.time.Clock()
pygame.event.clear()
while True:
    screen.fill((0,0,0))

    texte = font.render(str(score), True, (255,255,255))
    esp = font.size(str(score))
    screen.blit(texte, (400 - (esp[0]/2), 10))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            else:
                player.jump()
    toucher = player.update(clock.get_time(), RESO)
    print(spike) if type(toucher) == bool else None
    score = calcule_score(score, toucher)

    spike.affichage(screen, RESO)
    player.affichage(screen)
    pygame.display.flip()
    clock.tick(FPS)
