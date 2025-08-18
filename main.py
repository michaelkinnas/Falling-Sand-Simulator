import pygame
import sys
import random


WIDTH = 1600
HEIGHT = 1200
CELL_SIZE = 4
BRUSH_SIZE = 9
FPS = 60


# === Colors ===
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (120, 120, 120)


def setup():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Falling Sand Simulator")
    return screen


def draw_grid(grid, surface, cell_size):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] is not None:
                pygame.draw.rect(
                    surface=surface,
                    color=grid[i][j],
                    rect=pygame.Rect(
                        j * cell_size, i * cell_size, cell_size, cell_size
                    ),
                )


def update_grid(grid):
    rows = len(grid)
    cols = len(grid[0])

    new_grid = [[None for _ in range(cols)] for _ in range(rows)]

    for i in range(rows - 1, -1, -1):
        # Shuffle column order each row
        col_indices = list(range(cols))
        random.shuffle(col_indices)

        for j in col_indices:
            particle = grid[i][j]
            if particle is None:
                continue

            moved = False

            # Move down if possible
            if i + 1 < rows and grid[i + 1][j] is None and new_grid[i + 1][j] is None:
                new_grid[i + 1][j] = particle
                moved = True
            else:
                left_free = (
                    i + 1 < rows
                    and j - 1 >= 0
                    and grid[i + 1][j - 1] is None
                    and new_grid[i + 1][j - 1] is None
                )
                right_free = (
                    i + 1 < rows
                    and j + 1 < cols
                    and grid[i + 1][j + 1] is None
                    and new_grid[i + 1][j + 1] is None
                )

                if left_free and right_free:
                    if random.random() < 0.5:
                        new_grid[i + 1][j - 1] = particle
                    else:
                        new_grid[i + 1][j + 1] = particle
                    moved = True
                elif left_free:
                    new_grid[i + 1][j - 1] = particle
                    moved = True
                elif right_free:
                    new_grid[i + 1][j + 1] = particle
                    moved = True

            if not moved:
                new_grid[i][j] = particle

    return new_grid


def create_particle(grid, x, y, value, brush_size):
    for i in range(y - brush_size, y + brush_size + 1):
        if i >= 0 and i < len(grid):
            for j in range(x - brush_size, x + brush_size + 1):
                if j >= 0 and j < len(grid[i]):
                    grid[i][j] = value


def main():
    frame_count = 0

    screen = setup()
    clock = pygame.time.Clock()

    grid = [
        [None for _ in range(WIDTH // CELL_SIZE)] for _ in range(HEIGHT // CELL_SIZE)
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        # get mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        color = (
            frame_count,
            frame_count,
            frame_count,
        )

        if pygame.mouse.get_pressed()[0]:
            create_particle(
                grid,
                mouse_x // CELL_SIZE,
                mouse_y // CELL_SIZE,
                value=color,
                brush_size=BRUSH_SIZE,
            )

        grid = update_grid(grid)

        draw_grid(grid, screen, CELL_SIZE)

        pygame.display.flip()
        clock.tick(FPS)

        frame_count += 1
        frame_count %= 255


if __name__ == "__main__":
    main()
