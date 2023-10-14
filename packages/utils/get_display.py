import pygame


def get_display():
    resolution = pygame.display.Info()
    return resolution.current_w, resolution.current_h
