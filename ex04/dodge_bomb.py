import random
import pygame as pg
import sys
import tkinter as tk
import tkinter.messagebox as tkm
import datetime


st = datetime.datetime.now() 
def main():
    pg.display.set_caption("逃げろ！こうかとん") #ディスプレイ表示
    screen = pg.display.set_mode((1600, 900))
    scr_rect = screen.get_rect() # rect
    bg = pg.image.load("pg_bg.jpg").convert_alpha() # surfaceクラス
    rect_bg = bg.get_rect() # rectクラス
    num = random.randint(0, 8) #こうかとんの画像をランダムで選ぶ
    tori_img = pg.image.load(f"fig/{num}.png") 
    tori_img = pg.transform.rotozoom(tori_img, 0, 2.0)
    tori_rect = tori_img.get_rect()
    tori_rect.center = 900, 400
    vx1, vy1 = 1, -1 #移動速度
    vx2, vy2 = -1, 1 #移動速度

    # 2つの爆弾の表示
    image1 = pg.Surface((20, 20)) 
    image1.set_colorkey((0, 0, 0))
    image2 = pg.Surface((100, 100))
    image2.set_colorkey((0, 0, 0))
    image_rect1 = image1.get_rect()
    image_rect2 = image2.get_rect()
    image_rect1.centerx = random.randint(0, 1600)
    image_rect1.centery = random.randint(0, 900)
    image_rect2.centerx = random.randint(0, 1600)
    image_rect2.centery = random.randint(0, 900)
    pg.draw.circle(image1, (255, 0, 0), (10, 10), 10)
    pg.draw.circle(image2, (255, 0, 0), (50, 50), 50)





    while (1):
        clock = pg.time.Clock()

        
        pg.display.update()
        screen.blit(bg, rect_bg)

        # キーが押されたときにこうかとんを移動する
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            tori_rect.centery -= 1

        if key_lst[pg.K_DOWN]:
            tori_rect.centery += 1

        if key_lst[pg.K_RIGHT]:
            tori_rect.centerx += 1

        if key_lst[pg.K_LEFT]:
            tori_rect.centerx -= 1
        
        # こうかとんが領域外に出ないようにする
        if check_bound(tori_rect, scr_rect) != (1, 1):
            if key_lst[pg.K_UP]:
                tori_rect.centery += 1

            if key_lst[pg.K_DOWN]:
                tori_rect.centery -= 1

            if key_lst[pg.K_RIGHT]:
                tori_rect.centerx -= 1

            if key_lst[pg.K_LEFT]:
                tori_rect.centerx += 1          
        screen.blit(tori_img, tori_rect)

        image_rect1.move_ip(vx1,vy1)
        screen.blit(image1, image_rect1)
        image_rect2.move_ip(vx2,vy2)
        screen.blit(image2, image_rect2)

        # ×ボタンとエスケープキーが押されたときに閉じる
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                if event.key == pg.K_DELETE:
                    pg.quit()
                    sys.exit()
        
        # こうかとんと爆弾が接触したら閉じる
        if tori_rect.colliderect(image_rect1) or tori_rect.colliderect(image_rect2):
            gameover()
            return
        yoko1, tate1= check_bound(image_rect1, scr_rect)
        yoko2, tate2= check_bound(image_rect2, scr_rect)

        vx1*=yoko1
        vy1*=tate1
        vx2*=yoko2
        vy2*=tate2
        ed = datetime.datetime.now()
        time = f"{(ed-st).seconds}"
        # 経過時間を表示する
        fonto = pg.font.Font(None, 120)
        txt = fonto.render(str(time), True, (0, 0, 0))
        screen.blit(txt, (50, 50))

        pg.display.update()
        clock.tick(1000)
    
    # 壁に当たった時の判定
def check_bound(rct, scr_rct):
    x,y = 1, 1
    if scr_rct.left > rct.left or rct.right > scr_rct.right:
        x = -1

    if scr_rct.top > rct.top or rct.bottom > scr_rct.bottom:
        y = -1
    return x, y

    # ゲームオーバー時に表示する
def gameover():
    ed = datetime.datetime.now()
    time = f"{(ed-st).seconds}秒"
    tkm.showinfo("Game Over", f"タイムは{time}でした")


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
