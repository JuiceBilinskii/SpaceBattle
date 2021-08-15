import pygame
from abc import ABC, abstractmethod
from tortilla.extractor import ImageExtractor


class View(ABC):
    def __init__(self, screen: pygame.Surface):
        self._screen = screen
        # self.scale_factor = pygame.display.Info().current_w / 1920
        self._extractor = ImageExtractor()

    @abstractmethod
    def draw(self, model):
        pass
