import pygame
from abc import ABC, abstractmethod
from data.extractor import ImageExtractor
from data import constants


class IView(ABC):
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        # self.scale_factor = pygame.display.Info().current_w / 1920
        self.extractor = ImageExtractor()

    @abstractmethod
    def draw(self, model):
        pass
