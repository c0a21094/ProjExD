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
    while (1):
        pg.display.update()
        pg.time.wait(30)
        screen.fill((0, 20, 0, 0))
        screen.blit(bg, rect_bg)
        screen.blit(tori_img, tori_rect)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()