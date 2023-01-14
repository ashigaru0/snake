import pygame

from rules import Rules
from game import Game
from settings import Settings


class MainMenu:
    def __init__(self):
        self.menu_text = ['Начать игру', 'Правила', 'Настройки', 'Выход']  # Лучшие результаты - ?
        self.text_index = 0

        pygame.display.set_caption('Главное меню')
        self.size_screen = 500, 500
        self.screen = pygame.display.set_mode(self.size_screen)

    def check_menu_text(self, direction):
        self.text_index += 0 if (self.text_index == 0 and direction == -1) or \
                                (self.text_index == 3 and direction == 1) else direction

    def open_window(self):
        if self.text_index == 0:
            Game().running()

        elif self.text_index == 1:
            Rules().running()

        elif self.text_index == 2:
            pass  # Settings()

        else:
            pygame.quit()

    def render(self):
        # fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
        # self.screen.blit(pygame.Color('blue'), (0, 0))  # фон
        font = pygame.font.Font(None, 30)
        self.screen.fill((0, 0, 0))
        text_coord = 500 // 2 - 80
        for i, line in enumerate(self.menu_text):
            string_rendered = font.render(line, True, pygame.Color('white'))
            text_rect = string_rendered.get_rect()
            text_coord += 20
            text_rect.top = text_coord
            text_rect.x = 30
            text_coord += text_rect.height
            if i == self.text_index:
                pygame.draw.rect(self.screen, (61, 0, 153), text_rect)
            self.screen.blit(string_rendered, text_rect)
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    main_menu = MainMenu()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    main_menu.check_menu_text(-1)  # выбор опции, наверх
                elif event.key == pygame.K_s:
                    main_menu.check_menu_text(1)  # выбор опции, вниз
                elif event.key == pygame.K_RETURN:
                    main_menu.open_window()  # открытие нового окна

        main_menu.render()

    pygame.quit()

# import pygame

# from logics import snake_logics
# from render import board  # Вот это нужно переписать


# if __name__ == '__main__':
#     pygame.init()
#     size = (8, 12)

#     game = snake_logics(size=size, thrgh_walls=False, thrgh_self=False)
#     # thrgh_walls - возможность проходить сквозь стены
#     # thrgh_self - возможность проходить сквозь себя
#     # acceleration - изменение скорости в процентах
#     # speed - начальная скорость
#     # control_relatively_head - 2 режима управления(0 - глобальный; 1 - относительно головы)

#     brd = board(size_board=size, size_cell=50)

#     run = True
#     while run:
#         brd.add_cells(game.body)      # game.body - массив со всеми координатами ячеек змейки
#         brd.add_apple(game.apple)     # game.apple - координата яблока
#         brd.render()                  # Отрисовка

#         for event in pygame.event.get():
#             game.key_indexing(event)  # Отправляет все ивенты в класс змейки

#         run = game.run


