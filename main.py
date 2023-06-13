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
    def fire(self):
        bullets.add(Bullet('bullet.png',10,10,self.rect.right,self.rect.centery,2))

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
            if self.start_x >= self.rect.x:
                self.direction = 'right'

        else:
            self.rect.x += self.speed
            if self.end_x <= self.rect.x:
                self.direction = 'left'
class Bullet(Gamesprite):
    def __init__(self,picture,w,h,x,y,speed):
        Gamesprite.__init__(self,picture,w,h,x,y)
        self.speed = speed
    def update(self):
        self.reset()
        self.rect.x += self.speed 

       







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
player = Player('hero.png',50,50,170,170,0,0)
# enemy = Enemy('enemy.png',50,50,600,650,2,'left',600,700,0,0)
# enemy2 = Enemy('enemy.png',50,50,300,350,2,'left',320,400,0,0)
final = Gamesprite('teleport.png',70,70,1100,620)
win = Gamesprite('win.png',1200,700,0,0)
bullets = sprite.Group()
walls = sprite.Group()
walls.add(Gamesprite('walls.png',10,100,300,300))
walls.add(Gamesprite('walls.png',10,110,555,555))
walls.add(Gamesprite('walls.png',100,10,150,150))
walls.add(Gamesprite('walls.png',100,10,300,300))
walls.add(Gamesprite('walls.png',100,10,555,555))
walls.add(Gamesprite('walls.png',10,115,150,150))
walls.add(Gamesprite('walls.png',10,100,395,300))
walls.add(Gamesprite('walls.png',140,10,650,250))
walls.add(Gamesprite('walls.png',10,140,650,125))
walls.add(Gamesprite('walls.png',140,10,750,250))
walls.add(Gamesprite('walls.png',10,140,880,250))
# walls.add(Gamesprite('walls.png',20,150,300,300))
# walls.add(Gamesprite('walls.png',20,110,555,555))
# walls.add(Gamesprite('walls.png',100,20,150,150))
# walls.add(Gamesprite('walls.png',150,20,300,300))
# walls.add(Gamesprite('walls.png',100,20,555,555))
# walls.add(Gamesprite('walls.png',20,115,150,150))


enemys = []
enemys.append(Enemy('enemy.png',50,50,600,650,2,'left',600,700,0,0))
enemys.append(Enemy('enemy.png',50,50,300,350,2,'left',320,400,0,0))

sound1 = mixer.Sound('awp1.ogg')
sound2 = mixer.Sound('smert.ogg')
sound3 = mixer.Sound('winmusic.ogg')
mixer.music.load('fon_music.ogg')
mixer.music.play()

finish = False
player_speed = 5
while 1:

    if finish == False:
        window.blit(pic,(0,0))
        player.update()
        player.reset()
    
        bullets.update()
        
        final.reset()
    


    #platforms_touched = sprite.spritecollide (player, walls, False)
    for i in enemys:
        res = sprite.spritecollide(i,bullets,True)
        if len(res) != 0:
            enemys.remove(i)
            continue
        i.reset()
        i.update()
        if i.rect.colliderect(player.rect):
            player.rect.x = 170
            player.rect.y = 170
            sound2.play()

    for i in walls:
        i.reset()

    for i in event.get():
        if i.type == KEYDOWN:
            if i.key == K_SPACE:
                sound1.play()
                player.fire()
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
                sound3.play()
                finish = True    
        if i.type == QUIT:
            exit()

    clock.tick(40)
    display.update()
