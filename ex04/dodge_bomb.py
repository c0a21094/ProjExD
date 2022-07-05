import random
import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    bg = pg.image.load("pg_bg.jpg").convert_alpha() # surfaceクラス
    rect_bg = bg.get_rect()
    tori_img = pg.image.load("fig/6.png")
    tori_img = pg.transform.rotozoom(tori_img, 0, 2.0)
    tori_rect = tori_img.get_rect()
    tori_rect.center = 900, 400
    x = random.randint(0, 1600)
    y = random.randint(0, 900)
    vx, vy = 1, 1
    image = pg.Surface((20, 20))
    image.set_colorkey((0, 0, 0))
    pg.draw.circle(image, (255, 0, 0), (10, 10), 10)


    while (1):
        clock = pg.time.Clock()
        clock.tick(1000)
        
        pg.display.update()
        pg.time.wait(30)
        screen.fill((0, 20, 0, 0))
        screen.blit(bg, rect_bg)
        screen.blit(tori_img, tori_rect)
        screen.blit(image, (x, y))
        x += vx
        y += vy
        if x >= 1580:
            vx = -1
        elif x <= 0:
            vx = 1
        if y >= 880:
            vy = -1
        elif y <= 0:
            vy = 1

        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP] and tori_rect[1] >= 0:
            tori_rect.move_ip(0, -1)

        if key_lst[pg.K_DOWN] and tori_rect[1] <= 780:
            tori_rect.move_ip(0, 1)

        if key_lst[pg.K_RIGHT]and tori_rect[0] <= 1500:
            tori_rect.move_ip(1, 0)

        if key_lst[pg.K_LEFT]and tori_rect[0] >= 0:
            tori_rect.move_ip(-1, 0)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
        print(tori_rect)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
