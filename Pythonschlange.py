import pygame
import random

pygame.init()

# screen and window settings
window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Füttere die Python!")
screen_font = pygame.font.Font('./font/Snake Chan.ttf', 35)
score_font = pygame.font.SysFont('./font/Snake Chan.ttf', 20)
# colors
yellow = (204, 204, 0)
light_blue = (51, 153, 255)
red = (153, 0, 0)
green = (76, 153, 0)
lemon = (255, 255, 153)

clock = pygame.time.Clock()
python_speed = 20
# size of the smallest python element
python_piece = 10


def final_score(apples, meters):
    score_value = score_font.render(f"Ihr Ergebnis: {apples} Apfel / {meters} Meter", True, red)
    screen.blit(score_value, [0, 0])


def current_score(apples, meters):
    score_value = score_font.render(f"Pythonlange: {apples} Apfel / {meters} Meter", True, red)
    screen.blit(score_value, [0, 0])


def my_python(python_piece, python_list):
    for x in python_list:
        pygame.draw.rect(screen, yellow, [x[0], x[1], python_piece, python_piece])


def info(msg, color):
    message = screen_font.render(msg, True, color)
    text_rect = message.get_rect(center=(window_width / 2, window_height / 2))
    screen.blit(message, text_rect)


# game
def game_loop():
    game_over = False
    game_close = False
    # set python start position to the middle of the game window
    x1 = window_width / 2
    y1 = window_height / 2

    # variables for changing python coordinates
    x1_move = 0
    y1_move = 0

    python_list = []
    python_length = 1
    # growing apples for python food:
    apple_x = round(random.randrange(0, window_width - python_piece) / 10.0) * 10.0
    apple_y = round(random.randrange(0, window_height - python_piece) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(lemon)
            info("Die Python ist ausgeknockt!", red)
            final_score(python_length - 1, (python_length - 1) / 10.0)
            pygame.display.update()

            for action in pygame.event.get():
                if action.type == pygame.KEYDOWN:
                    if action.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if action.key == pygame.K_c:
                        game_loop()

        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                game_over = True
            if action.type == pygame.KEYDOWN:
                if action.key == pygame.K_a or action.key == pygame.K_LEFT:
                    x1_move = -python_piece
                    y1_move = 0
                elif action.key == pygame.K_d or action.key == pygame.K_RIGHT:
                    x1_move = python_piece
                    y1_move = 0
                elif action.key == pygame.K_w or action.key == pygame.K_UP:
                    x1_move = 0
                    y1_move = -python_piece
                elif action.key == pygame.K_s or action.key == pygame.K_DOWN:
                    x1_move = 0
                    y1_move = python_piece
            # preventing our python from kissing the walls:
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True
        x1 += x1_move
        y1 += y1_move
        screen.fill(light_blue)
        pygame.draw.rect(screen, green, [apple_x, apple_y, python_piece, python_piece])
        python_head = [x1, y1]
        python_list.append(python_head)

        if len(python_list) > python_length:
            del python_list[0]

        for x in python_list[:-1]:
            if x == python_head:
                game_close = True

        my_python(python_piece, python_list)
        current_score(python_length - 1, (python_length - 1) / 10.0)
        pygame.display.update()

        if x1 == apple_x and y1 == apple_y:
            apple_x = round(random.randrange(0, window_width - python_piece) / 10.0) * 10.0
            apple_y = round(random.randrange(0, window_height - python_piece) / 10.0) * 10.0
            python_length += 1

        clock.tick(python_speed)

    pygame.quit()
    quit()


if __name__ == '__main__':
    game_loop()
