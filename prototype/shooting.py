import pygame, sys, random, threading, math
from pygame.locals import *

bif = "bg.jpg"
bashiImage = "bashi.png"
pepe = "pepe.png"

pygame.init()
screen = pygame.display.set_mode((500, 500), 0, 32)
background = pygame.image.load(bif).convert()
bashi = pygame.image.load(bashiImage).convert_alpha()
pepe = pygame.image.load(pepe).convert_alpha()

myfont = pygame.font.SysFont("monospace", 18)

word = ""
enemys = []
words = ["jica", "zona", "tokonositel", "pn prehod", "tranzistor", "diod", "popravka"]
speed = 1.5
images = [pepe]
lost = False
highscore = 0
with open("highscore.txt", "r") as f: highscore = int(f.read())
score = 0



class Bashi:
    x = 250 - bashi.get_rect().size[0] / 2
    y = 500 - bashi.get_rect().size[1]


class Enemy:
    def __init__(self):
        self.word = r"jica"
        self.word = words[random.randint(0, len(words) - 1)]
        self.x = random.randint(0, 400)
        self.y = random.randint(0, 200)
        self.image = images[random.randint(0, len(images) - 1)]


def GenerateEnemys():
    threading.Timer(5, GenerateEnemys).start()
    for i in range(0, 7):
        enemys.append(Enemy())


GenerateEnemys()


def ToKillOrNotToKill():
    for enemy in enemys:
        if enemy.word == word:
            return True
    return False


def Kill():
    global score
    for enemy in enemys:
        if enemy.word == word:
            enemys.remove(enemy)
            score += 1
            return


def Move():
    threading.Timer(0.1, Move).start()
    for enemy in enemys:
        if (enemy.x < Bashi.x):
            enemy.x += speed
        elif (enemy.x > Bashi.x):
            enemy.x -= speed
        if (enemy.y < Bashi.y):
            enemy.y += speed


Move()


def SpeedUp():
    global speed
    threading.Timer(1, SpeedUp).start()
    speed += 0.1


SpeedUp()


def CheckForRIP():
    global Move
    global GenerateEnemys
    global SpeedUp
    for enemy in enemys:
        if (enemy.x - Bashi.x < speed + 1 and Bashi.y - enemy.y < 1):
            Move = None
            GenerateEnemys = None
            SpeedUp = None
            return True


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            GenerateEnemys = None
            SpeedUp = None
            Move = None
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            for enemy in enemys:
                print("--" + enemy.word)
        if event.type == KEYDOWN:
            if event.key == 13:
                while ToKillOrNotToKill():
                    Kill()
                word = ""
            elif event.key == 8:
                word = ''.join([word[x] for x in range(0, len(word) - 1)])
            else:
                word += chr(event.key)

    screen.blit(background, (0, 0))
    screen.blit(bashi, (Bashi.x, Bashi.y))
    scorelabel = myfont.render("Score: " + str(score), 1, (255, 255, 0))
    screen.blit(scorelabel, (0, 0))
    wordlabel = myfont.render("Word: " + word, 1, (255, 255, 0))
    screen.blit(wordlabel, (0, 21))


    for enemy in enemys:
        screen.blit(enemy.image, (enemy.x, enemy.y))
        curLabel = myfont.render(enemy.word, 1, (0, 0, 0))
        screen.blit(curLabel, (enemy.x, enemy.y))

    if (not lost) and CheckForRIP():
        lost = True

    if (lost):
        enemys = []
        loseLabel = myfont.render("U LOSE. SCORE = " + str(score), 1, (255, 0, 0))
        screen.blit(loseLabel, (175, 250))
        if(score>highscore):
            with open("highscore.txt", "w") as f: f.write(str(score))
            highscorelabel = myfont.render("NEW HIGHSCORE!", 1, (255, 0, 0))
            screen.blit(highscorelabel, (200, 271))

    pygame.display.update()
