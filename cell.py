import pygame


class Cell:
    def __init__(self, x, y, s):
        self.pos_x = x
        self.pos_y = y
        self.size = s

    def draw(self, screen):
        rect = pygame.Rect(self.pos_x + 1, self.pos_y + 1, self.size - 2, self.size - 2)
        pygame.draw.rect(screen, (200, 200, 200), rect)

        # entity = pygame.Rect(
        #     self.pos_x + 2, self.pos_y + 2, self.size - 4, self.size - 4
        # )
        # pygame.draw.ellipse(screen, (200, 0, 0), entity)
