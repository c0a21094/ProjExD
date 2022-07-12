
import pygame as pg
import sys
import random
import tkinter as tk
import tkinter.messagebox as tkm
import datetime



st = datetime.datetime.now() 

class Screen:
    def __init__(self, t, wh, fname):
        pg.display.set_caption(t)
        self.sfc = pg.display.set_mode(wh)        # Surface
        self.rct = self.sfc.get_rect()            # Rect
        self.bgi_sfc = pg.image.load(fname)       # Surface
        self.bgi_rct = self.bgi_sfc.get_rect()    # Rect

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    def __init__(self, fname: str, size: float, xy):
        self.sfc = pg.image.load(fname)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]: 
            self.rct.centery -= 1
        if key_states[pg.K_DOWN]: 
            self.rct.centery += 1
        if key_states[pg.K_LEFT]: 
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]:
            self.rct.centerx += 1
        # 練習7
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]: 
                self.rct.centery += 1
            if key_states[pg.K_DOWN]: 
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]: 
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT]: 
                self.rct.centerx -= 1
        self.blit(scr)

    def attack(self):
        return Shot(self)



class Bomb:
    def __init__(self, c, r, v, scr):
        self.sfc = pg.Surface((2*r, 2*r)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, c, (r, r), r)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = v # 練習6

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


class Shot:
    def __init__(self, chr: Bird):
        self.sfc = pg.image.load('beam.png')    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, 0.1)  # Surface
        self.rct = self.sfc.get_rect()
        self.rct.midleft = chr.rct.center
    
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
    def update(self, scr: Screen):
        self.rct.move_ip(+10, 0)
        if check_bound(self.rct, scr.rct) != (1,1):
            del self



class Enemy:
    def __init__(self, fname, xy, size, v, scr):
        self.sfc = pg.image.load(fname)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = v # 練習6

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


class End:
    def __init__(self):
        pg.mixer.init()
        pg.mixer.music.load("ちゃんちゃん♪2.mp3")
        pg.mixer.music.play(1)



class Bgm:
    def __init__(self):
        pg.mixer.music.load("Fly_With_Dreams.mp3")
        pg.mixer.music.play(-1)


def main():
    clock = pg.time.Clock()
    scr = Screen("負けるな！こうかとん", (1600, 900), "fig/pg_bg.jpg")
    kkimg = Bird("fig/6.png", 2.0, (900, 400))
    bmimg1 = Bomb((255, 150, 0), 50, (+1, +1), scr)
    bmimg2 = Bomb((255, 0, 150), 30, (+1.5, +1.5), scr)
    bmimg3 = Bomb((255, 0, 0), 10, (+2, +2), scr)

    enimg = Enemy("animal_bear_kowai.png", (100, 100), 0.1, (+3, +3), scr)
    beam = None

    while True:
        scr.blit()

        # 練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                beam = kkimg.attack() #スペースキーが押されたらこうかとんがビームを打つ
        bmimg1.update(scr)
        bmimg2.update(scr)
        bmimg3.update(scr)

        kkimg.update(scr)
        enimg.update(scr)
        if beam:
            beam.update(scr)
        if kkimg.rct.colliderect(bmimg1.rct) or kkimg.rct.colliderect(bmimg2.rct) or kkimg.rct.colliderect(bmimg3.rct):
            gameover() 
            End()
            return 
        elif enimg.rct.colliderect(kkimg.rct):
            gameclear()
            return



        pg.display.update()
        clock.tick(1000)


# 練習7
def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate


def gameover():
    ed = datetime.datetime.now()
    time = f"{(ed-st).seconds}秒"
    pg.mixer.music.stop()
    tkm.showinfo("Game Over", f"タイムは{time}でした")

def gameclear():
    ed = datetime.datetime.now()
    time = f"{(ed-st).seconds}秒"
    pg.mixer.music.stop()
    pg.mixer.music.load("レベルアップ.mp3")
    pg.mixer.music.play(1)
    tkm.showinfo("Game Clear", f"{time}で捕まえました！！！")


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()