import pygame
import random

from defeat import Defeat
from victory import Victory


class SnakeLogics:
    def __init__(self, size=(8, 8), thrgh_walls=False, thrgh_self=False,
                 speed=500.0, acceleration=0, control_relatively_head=False):
        self.control = {'w': (pygame.K_w, pygame.K_UP),
                        'a': (pygame.K_a, pygame.K_LEFT),
                        's': (pygame.K_s, pygame.K_DOWN),
                        'd': (pygame.K_d, pygame.K_RIGHT)}

        self.size_screen = None
        self.screen = None

        self.run = True
        self.size = size

        self.speed = speed
        self.acceleration = acceleration

        self.control_relatively_head = control_relatively_head

        self.thrgh_walls = thrgh_walls
        self.thrgh_self = thrgh_self

        self.body = [(0, 0), (0, 1), (0, 2)]
        self.apple = None
        self.direction = 0  # 0 - DOWN; 1 - RIGHT; 2 - UP; 3 - LEFT
        self.old_direction = 0
        self.count = 0

        self.move_event = pygame.USEREVENT + 1  # Ивент движения
        self.add_apple_event = pygame.USEREVENT + 2  # Ивент создания яблока

        pygame.time.set_timer(self.move_event, int(speed))  # Таймер на ивент движения
        pygame.time.set_timer(self.add_apple_event, 1000)  # Таймер на ивент создания яблока

    def change_direction(self, key):
        if not self.control_relatively_head:
            self.change_direction_global(key)
        else:
            self.change_direction_relatively(key)

    def change_direction_global(self, key):
        if key in self.control['s'] and self.old_direction != 2:
            self.direction = 0
        elif key in self.control['d'] and self.old_direction != 3:
            self.direction = 1
        elif key in self.control['w'] and self.old_direction != 0:
            self.direction = 2
        elif key in self.control['a'] and self.old_direction != 1:
            self.direction = 3

    def change_direction_relatively(self, key):
        if self.direction == 0:
            if key in self.control['d']:
                self.direction = 3
            elif key in self.control['a']:
                self.direction = 1
        elif self.direction == 1:
            if key in self.control['d']:
                self.direction = 0
            elif key in self.control['a']:
                self.direction = 2
        elif self.direction == 2:
            if key in self.control['d']:
                self.direction = 1
            elif key in self.control['a']:
                self.direction = 3
        elif self.direction == 3:
            if key in self.control['d']:
                self.direction = 2
            elif key in self.control['a']:
                self.direction = 0

    def out_of_size(self):
        if self.thrgh_walls is False:
            for cell in self.body:
                if ((cell[0] >= self.size[0] or cell[0] < 0) or
                        (cell[1] >= self.size[1] or cell[1] < 0)):
                    self.run = False
                    # поражение
                    defeat = Defeat('врезались в стену', self.count)  # результат/кол-во очков
                    defeat.running()

        else:
            for num, cell in enumerate(self.body):
                self.body[num] = (cell[0] % self.size[0], cell[1] % self.size[1])

    def collision(self):
        if self.thrgh_self is False:
            for cell in self.body[:-2:]:
                if self.body[-1] == cell:
                    self.run = False
                    # поражение
                    defeat = Defeat('врезались в себя', self.count)
                    defeat.running()

    def eat_apple(self):
        if self.apple == self.body[-1]:
            self.apple = None
            self.body.insert(0, self.body[0])
            self.speed -= (self.acceleration / 100) * self.speed
            self.count += 10

    def victory(self):
        if len(self.body) == self.size[0] * self.size[1]:
            self.run = False
            vc = Victory('Поздравляю!', self.count)
            vc.running()

    def move(self):
        del self.body[0]
        if self.direction == 0:
            self.body.append((self.body[-1][0], self.body[-1][1] + 1))
        if self.direction == 1:
            self.body.append((self.body[-1][0] + 1, self.body[-1][1]))
        if self.direction == 2:
            self.body.append((self.body[-1][0], self.body[-1][1] - 1))
        if self.direction == 3:
            self.body.append((self.body[-1][0] - 1, self.body[-1][1]))

        self.old_direction = self.direction

        self.victory()
        self.eat_apple()
        self.out_of_size()
        self.collision()

        pygame.time.set_timer(self.move_event, int(self.speed))

    def add_apple(self):
        if not self.apple:
            probabilities = [(x, y) for x in range(self.size[0]) for y in range(self.size[1])]
            for cell in self.body:
                if cell in probabilities:
                    probabilities.remove(cell)

            self.apple = random.choice(probabilities)

    def key_indexing(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d,
                             pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT]:
                self.change_direction(event.key)
            elif event.key == pygame.K_ESCAPE:
                self.run = False
                pygame.display.set_caption('Главное меню')
                self.size_screen = 500, 500
                self.screen = pygame.display.set_mode(self.size_screen)
        elif event.type == pygame.QUIT:
            self.run = False
            # возвращение в главное меню
            pygame.display.set_caption('Главное меню')
            self.size_screen = 500, 500
            self.screen = pygame.display.set_mode(self.size_screen)
        elif event.type == self.move_event:
            self.move()
        elif event.type == self.add_apple_event:
            self.add_apple()
