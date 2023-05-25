from settings import *

pg.font.init()
screen = pg.display.set_mode((700, 720))
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pg.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self) -> bool:
        pos = pg.mouse.get_pos()
        screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1:
                return True
        return False

class Menu:
    def __init__(self):
        self.start = Button(WIN_W * 0.5, WIN_H * 0.3, pg.image.load('assets/images/start.png').convert_alpha(), 0.5)
        self.end = Button(WIN_W * 0.5, WIN_H * 0.5, pg.image.load('assets/images/stop.png').convert_alpha(), 0.5)
    def run(self, score):
        check = False
        font = pg.font.SysFont("arialBlack", 18)
        img = font.render(f"Max Score {score}: ", True, (255, 255, 255))
        screen.blit(img, (WIN_W * 0.5, WIN_H * 0.7))
        while not check:
            pg.display.update()
            for _ in pg.event.get():
                if self.start.draw():
                    check = True
                elif self.end.draw():
                    exit(0)
