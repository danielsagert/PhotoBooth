import sys

import pygame as pg


def countdown(counter):
    pg.init()
    info = pg.display.Info()
    screen = pg.display.set_mode((info.current_w, info.current_h), pg.FULLSCREEN)
    screen_rect = screen.get_rect()
    font = pg.font.Font(None, 700)
    clock = pg.time.Clock()
    color = (255, 0, 0)
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    done = True

        txt = font.render(str(counter), True, color)
        counter -= 1

        screen.fill((30, 30, 30))
        screen.blit(txt, txt.get_rect(center=screen_rect.center))

        pg.display.flip()
        clock.tick(1)

        if counter < 0:
            break

    pg.quit()


if __name__ == '__main__':
    countdown(3)
    sys.exit()
