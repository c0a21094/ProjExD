import pygame as pg
import sys
import random
import tkinter as tk
import tkinter.messagebox as tkm



class Screen:
    def __init__(self, t, wh, fname):
        pg.display.set_caption(t)
        self.sfc = pg.display.set_mode(wh)        # Surface
        self.rct = self.sfc.get_rect()            # Rect
        self.bgi_sfc = pg.image.load(fname)       # Surface
        self.bgi_rct = self.bgi_sfc.get_rect()    # Rect

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Ball:
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

class Rect:
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

        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]: 
                self.rct.centery += 1
            if key_states[pg.K_DOWN]: 
                self.rct.centery -= 1

        self.blit(scr)


class Rect2:
    def __init__(self, fname: str, size: float, xy):
        self.sfc = pg.image.load(fname)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_w]: 
            self.rct.centery -= 1
        if key_states[pg.K_s]: 
            self.rct.centery += 1

        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_w]: 
                self.rct.centery += 1
            if key_states[pg.K_s]: 
                self.rct.centery -= 1

        self.blit(scr)


class Score: 
    def __init__(self, score1, score2):
        self.font = pg.font.Font("fig/font.ttf", 100)
        self.txt = self.font.render(f"{score1}    {score2}", True, (255, 255, 255))
        self.rct = self.txt.get_rect()
        
    def blit(self, scr: Screen):
        scr.sfc.blit(self.txt, (700, 150))

    def update(self, scr: Screen):
        self.blit(scr)


class Bgm:
    def __init__(self):
        pg.mixer.music.load("Fly_With_Dreams.mp3")
        pg.mixer.music.play(-1)


def main():
    r_score, l_score = 0, 0

    clock = pg.time.Clock()
    scr = Screen("エアホッケー", (1600, 890), "fig/bg.jpg")
    baimg = Ball((255, 0, 0), 30, (+2, +2), scr)
    reimg = Rect("fig/line2.jpeg", 0.7, (1575, 400))
    reimg2 = Rect2("fig/line-1.jpeg", 0.7, (25, 400))
    score = Score(l_score, r_score)
    Bgm()
    while True:
        scr.blit()
        score.blit(scr)

        for event in pg.event.get(): # ×ボタンが押されたらウィンドウを閉じる
            if event.type == pg.QUIT: return

        if baimg.rct.colliderect(reimg.rct): # 棒と接触したら跳ね返す
            baimg.vx *= -1

        if baimg.rct.colliderect(reimg2.rct): # 棒と接触したら跳ね返す
            baimg.vx *= -1

        baimg.update(scr)
        reimg.update(scr)
        reimg2.update(scr)
        score.update(scr)

        if baimg.rct.left < scr.rct.left : # 左側の壁に当たったら右側の得点を1プラスする
            r_score += 1
            score = Score(l_score, r_score)

        if baimg.rct.right > scr.rct.right : # 右側の壁に当たったら左側の得点を1プラスする
            l_score += 1
            score = Score(l_score, r_score)

        if r_score == 5:  # スコアが5点になったらメッセージを出して終了する
            pg.mixer.music.stop()
            pg.mixer.music.load("fig/レベルアップ.mp3")
            pg.mixer.music.play(1)
            tkm.showinfo("Game Clear", "Player2 Win!!")
            return 

        if l_score == 5: # スコアが5点になったらメッセージを出して終了する
            pg.mixer.music.stop()
            pg.mixer.music.load("fig/レベルアップ.mp3")
            pg.mixer.music.play(1)
            tkm.showinfo("Game Clear", "Player1 Win!!")
            return

        pg.display.update()
        clock.tick(1000)


def check_bound(rct, scr_rct):
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()