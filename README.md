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
    def update (self):
        self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide (player, walls, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min (self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)                
        self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide (player, walls, False)
        if self.y_speed > 0:
            for p in platforms_touched:
                self.rect.bottom = min (self.rect.bottom, p.rect.top)
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)    
class Enemy(Gamesprite):
    def __init__(self,picture,w,h,x,y,speed,direction,x1,x2,y1,y2):
        Gamesprite.__init__(self,picture,w,h,x,y)
        self.speed = speed 
        self.direction = direction 
        self.start_x = x1
        self.end_x = x2
        self.start_y = y1
        self.end_y = y2
    
    def update(self):
        if self.direction == 'left':
            self.rect.x -= self.speed
            if self.end_x >= self.rect.x:
                self.direction == 'right'

        else:
            self.rect.x += self.speed

        if self.direction == 'left':
            self.rect.y -= self.speed
            if self.end_y >= self.rect.y:
                self.direction == 'right'

        else:
            self.rect.y += self.speed







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
player = Player('hero.png',50,50,400,400,0,0)
enemy = Enemy('enemy.png',50,50,600,600,100,'left',350,250,0,0)
final = Gamesprite('teleport.png',70,70,1100,620)
win = Gamesprite('win.png',1200,700,0,0)

walls = sprite.Group()
walls.add(Gamesprite('walls.png',20,150,300,300))
walls.add(Gamesprite('walls.png',20,110,555,555))
walls.add(Gamesprite('walls.png',100,20,150,150))
walls.add(Gamesprite('walls.png',150,20,300,300))
walls.add(Gamesprite('walls.png',100,20,555,555))
walls.add(Gamesprite('walls.png',20,115,150,150))

sound1 = mixer.Sound('awp1.ogg')

mixer.music.load('fon_music.ogg')
mixer.music.play()

finish = False
player_speed = 5
while 1:
    
    if finish == False:
        window.blit(pic,(0,0))
        player.update()
        player.reset()
        enemy.reset()
        final.reset()
    for i in walls:
        i.reset()
    
    for i in event.get():
        if i.type == KEYDOWN:
            if i.key == K_SPACE:
                sound1.play()
            if i.key == K_d:
                player.x_speed += player_speed
            elif i.key == K_a:
                player.x_speed -= player_speed
            elif i.key == K_w:
                player.y_speed -= player_speed
            elif i.key == K_s:
                player.y_speed += player_speed
        elif i.type == KEYUP:
            if i.key == K_d:
                player.x_speed = 0
            elif i.key == K_a:
                player.x_speed = 0
            elif i.key == K_w:
                player.y_speed = 0
            elif i.key == K_s:
                player.y_speed = 0
    
            if sprite.collide_rect(player,final):
                win.reset()    
                finish = True    
        if i.type == QUIT:
            exit()
    
    clock.tick(40)
    display.update()
