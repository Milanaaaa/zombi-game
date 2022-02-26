import pygame
import random


def inter(x1, y1, x2, y2, db1, db2):
    self_x1 = x1
    self_x2 = x1 + db1
    self_y1 = y1
    self_y2 = y1 + db1

    other_x1 = x2
    other_x2 = x2 + db2
    other_y1 = y2
    other_y2 = y2 + db2

    s1 = (self_x1 > other_x1 and self_x1 < other_x2) or (self_x2 > other_x1 and self_x2 < other_x2)
    s2 = (self_y1 > other_y1 and self_y1 < other_y2) or (self_y2 > other_y1 and self_y2 < other_y2)
    s3 = (other_x1 > self_x1 and other_x1 < self_x2) or (other_x2 > self_x1 and other_x2 < self_x2)
    s4 = (other_y1 > self_y1 and other_y1 < self_y2) or (other_y2 > self_y1 and other_y2 < self_y2)
    if ((s1 and s2) or (s3 and s4)) or ((s1 and s4) or (s3 and s2)):
        return True
    else:
        return False


class Zombi:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.img = pygame.image.load(image)
        self.shape = pygame.Surface((40, 40))
        self.speed = random.choice((0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1))


pygame.init()

window = pygame.display.set_mode((400, 400))
screen = pygame.Surface((400, 400))
player = pygame.Surface((40, 40))

player.set_colorkey((0, 0, 0))

img_p = pygame.image.load('zombipad_images/player_zombi.png')
img_bg = pygame.image.load('zombipad_images/bg_zombi.png')
zombi_pics = ['zombipad_images/enemy1.png', 'zombipad_images/enemy2.png', 'zombipad_images/enemy3.png',
              'zombipad_images/enemy4.png', 'zombipad_images/enemy5.png']

count = 0
my_font = pygame.font.SysFont('monospace', 15)

z_x = 0
z_y = 0

p_x = 200
p_y = 360

done = False
game_over = False

monsters = []

while not done:
    if not game_over and len(monsters) < 5:
        z_x = random.randrange(360)
        z_y = 0
        pic = random.choice(zombi_pics)
        monsters.append(Zombi(z_x, z_y, pic))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = True
        # if e.type == pygame.KEYDOWN and e.key == pygame.K_s:
        #     p_y += 10
        # if e.type == pygame.KEYDOWN and e.key == pygame.K_w:
        #     p_y -= 10
        if e.type == pygame.KEYDOWN and e.key == pygame.K_a:
            p_x -= 10
        if e.type == pygame.KEYDOWN and e.key == pygame.K_d:
            p_x += 10
    for z in monsters:
        if inter(z.x, z.y, p_x, p_y, 40, 40):
            strike = False
            p_x = 2000
            p_y = 2000
            z.x = 1000
            z.y = 1000
            game_over = True
            string = my_font.render('Очков: ' + str(count) + ', вы проиграли', 0, (255, 0, 0))

    for m in monsters:
        m.y += m.speed
        if m.y > 400:
            m.x = 1000
            m.y = 1000
            monsters.pop(monsters.index(m))
            count += 1
    if not game_over:
        string = my_font.render('Очков: ' + str(count), 0, (0, 0, 0))

    screen.blit(img_bg, (0, 0))
    player.blit(img_p, (0, 0))

    for m in monsters:
        m.shape.set_colorkey((0, 0, 0))
        m.shape.blit(m.img, (0, 0))
        screen.blit(m.shape, (m.x, m.y))

    screen.blit(string, (0, 50))
    screen.blit(player, (p_x, p_y))
    window.blit(screen, (0, 0))
    pygame.display.update()

pygame.quit()
