import pygame

from sprite import SpritesClassic


class Board:
    def __init__(self, size_board=(8, 8), size_cell=100):
        self.size_cell = size_cell
        self.size_screen = (size_cell * size_board[0], size_cell * size_board[1])
        self.size_board = size_board

        self.screen = pygame.display.set_mode(self.size_screen)
        self.board = []

    def add_apple(self, apple):
        if apple:
            self.board[apple[1]][apple[0]] = 3

    def add_cells(self, cells):
        self.board = [[0] * self.size_board[0] for _ in range(self.size_board[1])]
        for num, cell in enumerate(cells):
            if num == len(cells) - 1:
                self.board[cell[1]][cell[0]] = 2
            else:
                self.board[cell[1]][cell[0]] = 1

    def render(self):
        image = pygame.image.load('backgrounds_img/background1_game.png')
        image = pygame.transform.scale(image, (int(self.size_screen[0] if self.size_screen[0] > 1000 else 1000),
                                               int(self.size_screen[1] if self.size_screen[1] > 1000 else 1000)))
        self.screen.blit(image, (0, 0))
        for h, data in enumerate(self.board):
            for w, color in enumerate(data):
                x, y = w * self.size_cell, \
                       h * self.size_cell

                if color == 1:  # тело змейки
                    self.screen.blit(SpritesClassic(self.size_cell).snakes_parts_b(), (x, y))
                elif color == 2:  # голова змейки
                    self.screen.blit(SpritesClassic(self.size_cell).snakes_parts_h(), (x, y))
                elif color == 3:  # голубика (apple или blueberry - зависит от класса)
                    self.screen.blit(SpritesClassic(self.size_cell).changed_image(), (x, y))
        pygame.display.flip()
