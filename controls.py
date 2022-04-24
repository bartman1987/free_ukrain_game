import pygame
import sys
from bullet import Bullet
from putin import Putin
import time


def events(screen, gun, bullets):
    """обработка события"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # вправо
            if event.key == pygame.K_d:
                gun.mright = True
            # лево
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            # вправо
            if event.key == pygame.K_d:
                gun.mright = False
            # лево
            elif event.key == pygame.K_a:
                gun.mleft = False


def update(bg_color, screen, gun, putins, bullets):
    """обновление экрана"""
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    putins.draw(screen)
    pygame.display.flip()


def update_bullets(putins, bullets):
    """обновляет позиции пуль"""
    bullets.update()
    for bullet in bullets. copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, putins, True, True)


def gun_kill(stats, screen, gun, putins, bullets):
    """столкновение пушки и армии"""
    stats.guns_left -= 1
    putins.empty()
    bullets.empty()
    create_army(screen, putins)
    gun.create_gun()
    time.sleep(2)


def update_putins(stats, screen, gun, putins, bullets):
    """обновляет позицию путина"""
    putins.update()
    if pygame.sprite.spritecollideany(gun, putins):
        gun_kill(stats, screen, gun, putins, bullets)


def create_army(screen, putins):
    """создание армии путина"""
    putin = Putin(screen)
    putin_width = putin.rect.width
    number_putin_x = int((700 - 1 * putin_width) / putin_width)
    putin_height = putin.rect.height
    number_putin_y = int((800 - 100 - 2 * putin_height) / putin_height)

    for row_number in range(number_putin_y - 2):
        for putin_number in range(number_putin_x):
            putin = Putin(screen)
            putin.x = putin_width + (putin_width * putin_number)
            putin.y = putin_height + (putin_height * row_number)
            putin.rect.x = putin.x
            putin.rect.y = putin.rect.height + (putin.rect.height * row_number)
            putins.add(putin)
