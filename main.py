from pygame import*
from random import*
class Gamesprite(sprite.Sprite):
    def __init__(self,picture,w,h,x,y):
        super().__init__()
        self.image = transform.scale(image.load(picture),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
       window.blit(self.image,(self.rect.x,self.rect.y))
class Player(Gamesprite):
    def __init__(self,picture,w,h,x,y,x_speed,y_speed):
        Gamesprite.__init__(self,picture,w,h,x,y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed


init()

blue = (20,20,240)
orange = (200,200,0)
red = (200,0,0)
black = (0,0,0)
green = (0,255,0)
purple = (128,0,128)
height_win = 700
weight_win = 1200
pic = transform.scale(image.load('back.jpg'),(weight_win,height_win))

window = display.set_mode((weight_win,height_win))
clock = time.Clock()

player = Player('hero.png',50,70,400,400,0,0)

walls=[]
walls.append(Gamesprite('fon.png',20,150,300,300))
walls.append(Gamesprite('fon.png',20,70,555,555))
walls.append(Gamesprite('fon.png',100,20,150,150))





player_speed = 5
while 1:

    window.blit(pic,(0,0))
    player.update()
    player.reset()
    for i in walls:
        i.reset()
    for i in event.get():
        if i.type == QUIT:
            exit()
        if i.type == KEYDOWN:
            
            if i.key == K_d:
                player.x_speed += player_speed
            if i.key == K_a:
                player.x_speed -= player_speed
            if i.key == K_w:
                player.y_speed -= player_speed
            if i.key == K_s:
                player.y_speed += player_speed
        elif i.type == KEYUP:
            if i.key == K_d:
                player.x_speed = 0
            if i.key == K_a:
                player.x_speed = 0
            if i.key == K_w:
                player.y_speed = 0
            if i.key == K_s:
                player.y_speed = 0
    clock.tick(40)
    display.update()               