import pygame, controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores


def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Украинские защитники")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    putins = Group()
    controls.create_army(screen, putins)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, stats, sc, gun, putins, bullets)
            controls.update_bullets(screen, stats, sc, putins, bullets)
            controls.update_putins(stats, screen, gun, putins, bullets)


run()
