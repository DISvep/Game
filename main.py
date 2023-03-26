from pygame import *
from pygame import mixer as m

init()
m.init()

window = display.set_mode((700, 500))

display.set_caption("Лабiрiнт")

bg = transform.scale(image.load("Textures\\map.png"), (700, 500))
player = transform.scale(image.load("Textures\\hero.png"), (50, 50))

m.music.load("Textures\\jungles.ogg")
m.music.play()
code = False
codeWIN = False
gameOVER = False


class Player(sprite.Sprite):
    def __init__(self, img, x, y, speed, f=False, razgon=180):
        super().__init__()
        if f:
            self.img = transform.scale(image.load(img), (90, 90))
        else:
            self.img = transform.scale(image.load(img), (50, 50))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self._right = True
        self.otchet = razgon

    def draw_sprite(self):
        window.blit(self.img, (self.rect.x, self.rect.y))

    def enemy_update(self, razgon):
        if self._right and self.otchet > 0:
            self.rect.x += self.speed
            self.otchet -= self.speed
        if not self._right and self.otchet > 0:
            self.rect.x -= self.speed
            self.otchet -= self.speed
        if self.otchet <= 0:
            self.otchet = razgon
            self._right = not self._right

    def update(self):
        pressed_key = key.get_pressed()
        if pressed_key[K_BACKSLASH]:
            global code, codeWIN, text_, textRect, font_
            code = True
            codeWIN = rectangle(100, 200, cod=True)
            font_ = font.SysFont("ComicSansMC", 50)
            text_ = font_.render("", True, (255, 255, 255), None)
            textRect = text_.get_rect()
        if not gameOVER:
            if pressed_key[K_w]:
                player.up()
            if pressed_key[K_s]:
                player.down()
            if pressed_key[K_d]:
                player.right()
            if pressed_key[K_a]:
                player.left()

    def up(self):
        if self.rect.y > 0:
            self.rect.y -= self.speed

    def down(self):
        if self.rect.y < 450:
           self.rect.y += self.speed

    def left(self):
        if self.rect.x > 0:
            self.rect.x -= self.speed

    def right(self):
        if self.rect.x < 630:
            self.rect.x += self.speed


class rectangle(sprite.Sprite):
    def __init__(self, x, y, cod=False):
        super().__init__()
        if cod:
            self.obj = Surface((500, 50))  # Surface((300, 50))
            self.obj.fill((0, 0, 0))
        else:
            self.obj = Surface((50, 50))
            self.obj.fill((255, 0, 0))
        self.rect = self.obj.get_rect()
        self.rect.x = x
        self.rect.y = y

    def render(self):
        window.blit(self.obj, (self.rect.x, self.rect.y))


map = [
    [
        [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0]
    ],
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    ],
    [
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    [
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]
    ],
    [
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0]
    ],
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
    ]

]
walls = []


player = Player("Textures\\hero.png", 0, 0, 3)
enemy = Player("Textures\\cyborg.png", 450, 300, 3)
win = Player("Textures\\treasure.png", 540, 400, 0, f=True)
razgon = 180


def map_gen(lvl):
    global walls, enemy, win, razgon

    if lvl == 1:
        del enemy
        enemy = Player("Textures\\cyborg.png", 230, 100, 3, razgon=180)
        razgon = 100
        win.rect.x, win.rect.y = 610, 10
    elif lvl == 2:
        del enemy
        win.rect.x, win.rect.y = 610, 355
    elif lvl == 3:
        enemy = Player("Textures\\cyborg.png", 550, 100, 3, razgon=110)
        razgon = 110
        win.rect.x, win.rect.y = 580, 10
    elif lvl == 4:
        del enemy
        enemy = Player("Textures\\cyborg.png", 550, 350, 2, razgon=110)
        razgon = 110
        win.rect.x, win.rect.y = 580, 400
    elif lvl == 5:
        del enemy
        win.rect.x, win.rect.y = 600, 400
    if walls != []:
        walls = []

    ynum = 0
    for y in map[lvl]:
        num = 0
        for x in y:
            if x == 1:
                a = rectangle(num*50, ynum*50)
                walls.append(a)
            num += 1
        ynum += 1


map_gen(lvl=0)
lvl = 0

text = ''
clock = time.Clock()
game = True
while game:
    window.blit(bg, (0, 0))
    player.draw_sprite()
    if lvl != 2 and lvl != 5:
        enemy.draw_sprite()
    win.draw_sprite()

    for e in event.get():
        if e.type == QUIT:
            game = False
        if code and e.type == KEYDOWN:
            if e.key == K_RETURN:
                if code and codeWIN:
                    if text == 'golvl1':
                        lvl = 1
                        map_gen(lvl)
                        codeWIN = False
                        # del font_, text_, textRect
                    elif text == 'golvl2':
                        lvl = 2
                        map_gen(lvl)
                        codeWIN = False
                    elif text == 'golvl3':
                        lvl = 3
                        map_gen(lvl)
                        codeWIN = False
                    elif text == 'golvl4':
                        lvl = 4
                        map_gen(lvl)
                        codeWIN = False
                    elif text == 'golvl5':
                        lvl = 5
                        map_gen(lvl)
                        codeWIN = False
                        # del font_, text_, textRect
                    text = ''
                    code = False
                    codeWIN = False
                    # del font_, text_, textRect
            elif e.key == K_BACKSPACE:
                text = text[:-1]
            else:
                text += e.unicode

    for i in walls:
        i.render()

    if codeWIN != False:
        codeWIN.render()
        text_ = font_.render(text, True, (255, 255, 255), (0, 0, 0))
        textRect = text_.get_rect()
        textRect.x, textRect.y = 100, 200
        window.blit(text_, textRect)

    death = False
    if not lvl == 2 and not lvl == 5:
        death = Rect.colliderect(player.rect, enemy.rect)
    if death:
        player.rect.x, player.rect.y = 0, 0
        m.Channel(1).play(mixer.Sound("Textures\\kick.ogg"))
    death = False
    for i in walls:
        if Rect.colliderect(player.rect, i.rect):
            death = True
            break
    if death:
        player.rect.x, player.rect.y = 0, 0
        m.Channel(1).play(mixer.Sound("Textures\\kick.ogg"))
    winner = Rect.colliderect(player.rect, win.rect)
    if winner:
        if lvl != 5:
            m.Channel(1).play(mixer.Sound("cashier-quotka-chingquot-sound-effect-129698.ogg"))
            player.rect.x, player.rect.y = 0, 0
            lvl += 1
            map_gen(lvl=lvl)
        else:
            font__ = font.SysFont("ComicSansMC", 200)
            text__ = font__.render("YOU WIN!", True, (255, 255, 0), None)
            textRect_ = text__.get_rect()
            textRect_.x, textRect_.y = 10, 150
            gameOVER = True
            window.blit(text__, textRect_)


    player.update()
    if not lvl == 2 and not lvl == 5:
        enemy.enemy_update(razgon)
    display.update()
    clock.tick(60)