import pygame

# initialize modules
pygame.init()
pygame.font.init()
pygame.mixer.init()

# pygame window setup
WIDTH, HEIGHT = 1000, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Combat")

# fonts setup
title_font = pygame.font.SysFont('comicsans', 70)
smallfont = pygame.font.SysFont('Corbel', 50)


# texts render
game_title = title_font.render("pygame combat", True, (187, 0, 0))
text = smallfont.render('Start', True, (255, 255, 255))
quit_text = smallfont.render('Quit', True, (255, 255, 255))\



def game():
    ingame = True

    while ingame:
        WINDOW.fill((0, 0, 0))
        for event in pygame.event.get():
            # handle events that happen on in game screen
            if event.type == pygame.QUIT:
                ingame = False
                exit()
        pygame.display.update()


def start():
    intro = True

    while intro:
        # display game title in the center
        WINDOW.blit(game_title, (WIDTH/2 - game_title.get_width() / 2, 40))

        # display start button
        button = pygame.draw.rect(WINDOW, (100, 100, 100), [420, 315, 160, 60])
        WINDOW.blit(text, (460, 330))

        # display quit button
        button2 = pygame.draw.rect(
            WINDOW, (100, 100, 100), [420, 415, 160, 60])
        WINDOW.blit(quit_text, (460, 430))

        for event in pygame.event.get():
            # handle events that happen on intro screen
            if event.type == pygame.QUIT:
                intro = False
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(pygame.mouse.get_pos()):
                    # mouseclick on  start button
                    intro = False
                    game()

                if button2.collidepoint(pygame.mouse.get_pos()):
                    # mouseclick on  quit button
                    intro = False
                    exit()

        pygame.display.update()


if __name__ == "__main__":
    start()
