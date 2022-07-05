import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    bg = pg.image.load("pg_bg.jpg").convert_alpha() # surfaceクラス
    bg = pg.transform.rotozoom(bg, 0, 1) # surface


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()