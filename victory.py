import pygame


class Victory:
    def __init__(self, text, count):
        self.text = ['Вы выиграли!', '', text, '', f'Ваш результат: {count}']

        self.size_screen = 500, 500
        self.screen = pygame.display.set_mode(self.size_screen)
        pygame.display.set_caption('Победа')

    def render(self):
        font = pygame.font.Font(None, 40)
        image = pygame.image.load('backgrounds_img/background_victory.png')
        fon = pygame.transform.scale(image, (500, 500))
        self.screen.blit(fon, (0, 0))  # фон
        text_coord = 20
        for i, line in enumerate(self.text):
            string_rendered = font.render(line, True, pygame.Color('white'))
            text_rect = string_rendered.get_rect()
            text_coord += 20
            text_rect.top = text_coord
            text_rect.x = 20
            text_coord += text_rect.height
            self.screen.blit(string_rendered, text_rect)
        # текст - выход с помощью Enter
        font_enter = pygame.font.Font(None, 20)
        text_rendered = font_enter.render('Нажмите Enter для выхода', True, pygame.Color('white'))
        text_rect = text_rendered.get_rect()
        text_width, text_height = font_enter.size('Нажмите Enter для выхода')
        text_rect.x, text_rect.y = 490 - text_width, 490 - text_height
        self.screen.blit(text_rendered, text_rect)
        pygame.display.flip()

    def running(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.display.set_caption('Главное меню')
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        running = False
                        pygame.display.set_caption('Главное меню')
            self.render()
        pygame.display.set_caption('Победа')
