import pygame


class Entity:
    def __init__(self, x, y, s, gene):
        self.pos_x = x
        self.pos_y = y
        self.size = s
        self.gene = gene

        # self.color
        # self.speed
        # self.direction

        self._parse_gene(gene)

    def draw(self, screen):
        # rect = pygame.Rect(self.pos_x + 1, self.pos_y + 1, self.size - 2, self.size - 2)
        # pygame.draw.rect(screen, (200, 200, 200), rect)

        entity = pygame.Rect(
            self.pos_x + 2, self.pos_y + 2, self.size - 4, self.size - 4
        )
        pygame.draw.ellipse(screen, self.color, entity)

    def _parse_gene(self, gene):
        self.speed = int(gene[:4], 2)
        self.direction = gene[4:6]
        self.color = (int(gene[0:8], 2), int(gene[8:16], 2), int(gene[16:24], 2))

    # dd: Direction: 00 North, 01 East, 11 South, 10 West
    def move(self):
        if self.direction == "00":
            self.pos_y -= self.size
        elif self.direction == "01":
            self.pos_x += self.size
        elif self.direction == "11":
            self.pos_y += self.size
        elif self.direction == "10":
            self.pos_x -= self.size
