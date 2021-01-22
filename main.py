import os
import platform
import sys
import pygame
from pygame import K_ESCAPE, K_F4, K_RALT, K_LALT, QUIT, KEYDOWN


# Initialization
if platform.system() == 'Windows':
    from ctypes import windll
    windll.user32.SetProcessDPIAware()
os.environ['SDL_VIDEO_CENTERED'] = '1'  # center display
pygame.init()
clock = pygame.time.Clock()

FULL_SCREEN = False


if __name__ == '__main__':
    # Screen
    if FULL_SCREEN:
        SCREEN_WIDTH = round(pygame.display.Info().current_w)
        SCREEN_HEIGHT = round(pygame.display.Info().current_h)
        SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
    else:
        SCREEN_WIDTH = round(pygame.display.Info().current_w * 0.75)
        SCREEN_HEIGHT = round(pygame.display.Info().current_h * 0.75)
        SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Main loop
    while True:
        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            alt_f4 = (event.type == KEYDOWN and (event.key == K_F4
                                                 and (pressed_keys[K_LALT] or pressed_keys[K_RALT])))
            if event.type == QUIT or alt_f4:
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pass

        pygame.display.update()
        clock.tick(30)
        print(str(clock.get_fps()))
