import random
import re
import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    scr_rect = screen.get_rect()
    bg = pg.image.load("pg_bg.jpg").convert_alpha() # surfaceクラス
    rect_bg = bg.get_rect() # rectクラス
    tori_img = pg.image.load("fig/6.png")
    tori_img = pg.transform.rotozoom(tori_img, 0, 2.0)
    tori_rect = tori_img.get_rect()
    tori_rect.center = 900, 400
    vx, vy = 1, 1
    image = pg.Surface((20, 20))
    image.set_colorkey((0, 0, 0))
    image_rect = image.get_rect()
    image_rect.centerx = random.randint(0, 1600)
    image_rect.centery = random.randint(0, 900)
    pg.draw.circle(image, (255, 0, 0), (10, 10), 10)


    while (1):
        clock = pg.time.Clock()

        
        pg.display.update()
        screen.blit(bg, rect_bg)

        # x += vx
        # y += vy
        # if x >= 1580:
        #     vx = -1
        # elif x <= 0:
        #     vx = 1
        # if y >= 880:
        #     vy = -1
        # elif y <= 0:
        #     vy = 1

        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            tori_rect.centery -= 1

        if key_lst[pg.K_DOWN]:
            tori_rect.centery += 1

        if key_lst[pg.K_RIGHT]:
            tori_rect.centerx += 1

        if key_lst[pg.K_LEFT]:
            tori_rect.centerx -= 1
        
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

        image_rect.move_ip(vx,vy)
        screen.blit(image, image_rect)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
        if tori_rect.colliderect(image_rect):
            return
        yoko, tate= check_bound(image_rect, scr_rect)
        vx*=yoko
        vy*=tate
        pg.display.update()
        clock.tick(1000)

def check_bound(rct, scr_rct):
    x,y = +1, +1
    if scr_rct.left > rct.left or rct.right > scr_rct.right:
        x = -1

    if scr_rct.top > rct.top or rct.bottom > scr_rct.bottom:
        y = -1
    return x, y

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
