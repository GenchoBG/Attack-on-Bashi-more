import pygame, sys, random, threading
from pygame.locals import *

bif = "bg.jpg"
bashiImage = "bashi.png"
pepe = "pepe.png"

pygame.init()
screen = pygame.display.set_mode((500, 500), 0, 32)
background = pygame.image.load(bif).convert()
bashi = pygame.image.load(bashiImage).convert_alpha()
pepe = pygame.image.load(pepe).convert_alpha()

myfont = pygame.font.SysFont("monospace", 15)

word = ""
enemys = []
words = ["jica", "zona", "tokonositel", "pn prehod", "tranzistor", "diod", "popravka"]

images = [pepe]


class Enemy:
    def __init__(self):
        self.word = r"jica"
        self.word = words[random.randint(0, len(words) - 1)]
        self.x = random.randint(0, 400)
        self.y = random.randint(0, 200)
        self.image = images[random.randint(0, len(images) - 1)]


for i in range(0, 10):
    enemys.append(Enemy())


def ToKillOrNotToKill():
    for enemy in enemys:
        if enemy.word == word:
            return True
    return False


def Kill():
    for enemy in enemys:
        if enemy.word == word:
            enemys.remove(enemy)
            print("KILL")
            return


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            for enemy in enemys:
                print("--" + enemy.word)
        if event.type == KEYDOWN:
            if (event.key) == 13:
                while ToKillOrNotToKill():
                    Kill()
                word = ""
            else:
                word += chr(event.key)

    screen.blit(background, (0, 0))
    screen.blit(bashi, (250 - bashi.get_rect().size[0] / 2, 500 - bashi.get_rect().size[1]))
    label = myfont.render(word, 1, (255, 255, 0))
    screen.blit(label, (0, 0))

    for enemy in enemys:
        screen.blit(enemy.image, (enemy.x, enemy.y))
        curLabel = myfont.render(enemy.word, 1, (0, 0, 0))
        screen.blit(curLabel, (enemy.x, enemy.y))

    pygame.display.update()
