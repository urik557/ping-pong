from pygame import *
font.init()

win_width = 700
win_height = 500
win = display.set_mode((win_width,win_height))
display.set_caption('Пинг-понг')


font1 = font.Font(None,30)
font2 = font.Font(None,70)
font_win = font2.render('YOU WIN!',True,(254,242,0))
font_lose = font2.render('YOU LOSE!',True,(255,19,0))
speed_x = 3
speed_y = 3
background = transform.scale(image.load('сцена.jpg'), (700,500))

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.size_x = size_x
        self.size_y = size_y

    
    def reset(self):
        win.blit(self.image,(self.rect.x,self.rect.y))


class Player(GameSprite):
    def go1(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
            
        if keys_pressed[K_RIGHT] and self.rect.x < 630:
            self.rect.x += self.speed
    
    def go2(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
            
        if keys_pressed[K_d] and self.rect.x < 630:
            self.rect.x += self.speed


platform1 = Player('platform.jpg',300,70,120,60,10)
platform2 = Player('platform.jpg',300,360,120,60,10)
ball = GameSprite('ball.png',300,200,50,50,5)

play_game = True
finish = False
while play_game:

    for i in event.get():
        if i.type == QUIT:
            play_game = False
    
    if not finish:
        win.blit(background,(0,0))
        platform1.reset()
        platform2.reset()
        platform1.go1()
        platform2.go2()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if sprite.collide_rect(ball,platform1):
        speed_y *= -1

    if sprite.collide_rect(ball,platform2):
        speed_y *= -1

    if ball.rect.x > 650 or ball.rect.x < 0:
        speed_x *= -1
    
    if ball.rect.y < (platform1.rect.y - 40):
        finish = True
        platform1_x = platform1.rect.x
        platform2_x = platform2.rect.x
        platform1_y = platform1.rect.y
        platform2_y = platform2.rect.y
        win.blit(font_lose,(platform1_x,platform1_y))
        win.blit(font_win,(platform2_x,platform2_y))

    if ball.rect.y > (platform2.rect.y + 40):
        finish = True
        platform1_x = platform1.rect.x
        platform2_x = platform2.rect.x
        platform1_y = platform1.rect.y
        platform2_y = platform2.rect.y
        win.blit(font_lose,(platform2_x,platform2_y))
        win.blit(font_win,(platform1_x,platform1_y))


    display.update()
    clock = time.Clock()
    clock.tick(60)